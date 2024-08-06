import pandas as pd
from tqdm import tqdm
import pytz
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.AutoFeeder import *
from api.serializers import *
from western.settings import *


REPORTS_URL = "https://marsapi.ams.usda.gov/services/v1.2/reports"


class UserPermissionCheckAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_superuser or user.is_staff:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "Access Forbidden"}, status=status.HTTP_403_FORBIDDEN
            )


class AddAuctionFromJSON(APIView):
    def get(self, request, id=None):
        try:
            with open("auction.json", "r") as f:
                data = json.load(f)
            serializer = AuctionSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

            else:
                return Response(
                    {"results": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )

        except ObjectDoesNotExist:
            return Response(
                {"error": "Auction not found"}, status=status.HTTP_404_NOT_FOUND
            )


class AuctionView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                auction = Auction.objects.get(id=id)
                serializer = AuctionSerializer(auction)
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

            else:
                auction = Auction.objects.all()
                serializer = AuctionSerializer(auction, many=True)
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Auction not found"}, status=status.HTTP_404_NOT_FOUND
            )


class UpdateView(APIView):
    def get(self, request, slug=None):
        try:
            auctions = Auction.objects.all()
            for auction in auctions:
                make_request(auction)
            return Response({"results": "serializer.data"}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Error updating"}, status=status.HTTP_404_NOT_FOUND
            )


class ReportView(APIView):
    def get(self, request, slug=None):
        try:
            response = requests.get(REPORTS_URL, auth=(os.getenv("MARS_API_KEY"), ""))
            reports = {obj["slug_id"]: obj for obj in response.json()}
            auctions = Auction.objects.all()

            update = []
            for auction in auctions:
                report_date = datetime.strptime(
                    reports[auction.slug]["published_date"], "%m/%d/%Y %H:%M:%S"
                )
                localized_datetime = pytz.timezone("UTC").localize(report_date)
                if localized_datetime > auction.report_date:
                    update.append(auction)

            for a in tqdm(update):
                make_request(a)

            return Response(
                {"data": "serializer.data"},
                status=status.HTTP_200_OK,
            )

        except ObjectDoesNotExist:
            return Response(
                {"error": "Error updating"}, status=status.HTTP_404_NOT_FOUND
            )

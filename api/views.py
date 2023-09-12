import pandas as pd
import asyncio
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.AutoFeeder import *
from api.serializers import *
from western.settings import *


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

    def post(self, request):
        serializer = AuctionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"results": serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response(
                {"results": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, id=None):
        try:
            auction = Auction.objects.get(id=id)
            serializer = AuctionSerializer(auction, data=request.data)
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

    def patch(self, request, id=None):
        try:
            auction = Auction.objects.get(id=id)
            serializer = AuctionSerializer(auction, data=request.data, partial=True)
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


class SaleView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                sale = Sale.objects.get(id=id)
                serializer = SaleSerializer(sale)
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

            else:
                sale = Sale.objects.all()
                serializer = SaleSerializer(sale, many=True)
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"results": serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response(
                {"results": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, id=None):
        try:
            sale = Sale.objects.get(id=id)
            serializer = SaleSerializer(sale, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

            else:
                return Response(
                    {"results": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )

        except ObjectDoesNotExist:
            return Response(
                {"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, id=None):
        try:
            sale = Sale.objects.get(id=id)
            serializer = SaleSerializer(sale, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

            else:
                return Response(
                    {"results": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )

        except ObjectDoesNotExist:
            return Response(
                {"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND
            )


class UpdateView(APIView):
    def get(self, request, slug=None):
        try:
            auction = Auction.objects.get(slug=slug)
            make_request(auction)
            return Response({"results": "serializer.data"}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Error updating"}, status=status.HTTP_404_NOT_FOUND
            )

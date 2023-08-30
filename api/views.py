import requests
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from django.shortcuts import redirect

from api.models import *
from api.serializers import *
from western.settings import *


class AuctionView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                auction = Auction.objects.get(id=id)
                serializer = AuctionSerializer(sale)
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

            else:
                sale = Sale.objects.all()
                serializer = AuctionSerializer(sale)
                return Response({"results": serializer.data}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND
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
                serializer = SaleSerializer(sale)
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

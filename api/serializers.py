from rest_framework import serializers

from .models import Sale, Auction


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    auction = AuctionSerializer()

    class Meta:
        model = Sale
        fields = "__all__"

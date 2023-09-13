from rest_framework import serializers

from .models import Sale, Auction


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    auction = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = "__all__"

    def get_auction(self, obj):
        return obj.auction.name

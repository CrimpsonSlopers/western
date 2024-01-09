from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Sale, Auction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_superuser', 'is_staff', "username", "first_name", "last_name", "email"]


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

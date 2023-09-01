from django.contrib import admin
from api.models import Auction, Sale


class AuctionAdmin(admin.ModelAdmin):
    list_display = ["slug", "name", "full_name", "market", "last_final_sale_date"]


class SaleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sale._meta.get_fields()]


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Sale, SaleAdmin)

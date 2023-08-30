from django.contrib import admin
from api.models import Auction, Sale


class SaleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sale._meta.get_fields()]


admin.site.register(Auction)
admin.site.register(Sale, SaleAdmin)

from django.contrib import admin
from api.models import Auction, Sale
from django.utils.translation import gettext_lazy as _


class AuctionAdmin(admin.ModelAdmin):
    list_display = [
        "slug",
        "name",
        "full_name",
        "market",
        "report_date",
        "report_status",
    ]
    list_filter = [
        "market",
        "report_status",
    ]
    search_fields = [
        "slug",
        "name",
        "full_name",
    ]


class IsTempListFilter(admin.SimpleListFilter):
    title = _("filter out finals")

    parameter_name = "preliminary"

    def lookups(self, request, model_admin):
        return [
            ("prelim", _("preliminary")),
            ("final", _("final")),
        ]

    def queryset(self, request, queryset):
        if self.value() == "prelim":
            return queryset.filter(final_ind="preliminary")
        if self.value() == "final":
            return queryset.filter(final_ind="final")


class SaleAdmin(admin.ModelAdmin):
    list_filter = [IsTempListFilter]
    search_fields = [
        "auction",
    ]
    list_display = (
        "date",
        "auction",
        "final_ind",
        "head1",
        "weight1_formatted",
        "price1_formatted",
        "head2",
        "weight2_formatted",
        "price2_formatted",
        "head3",
        "weight3_formatted",
        "price3_formatted",
        "head4",
        "weight4_formatted",
        "price4_formatted",
        "head5",
        "weight5_formatted",
        "price5_formatted",
        "region",
    )

    def auction_plus(self, obj):
        return f"{obj.auction} {obj.date}"

    def weight1_formatted(self, obj):
        return "{0:.2f}".format(obj.weight1)

    def price1_formatted(self, obj):
        return "{0:.2f}".format(obj.weight1)

    def weight2_formatted(self, obj):
        return "{0:.2f}".format(obj.weight2)

    def price2_formatted(self, obj):
        return "{0:.2f}".format(obj.price2)

    def weight3_formatted(self, obj):
        return "{0:.2f}".format(obj.weight3)

    def price3_formatted(self, obj):
        return "{0:.2f}".format(obj.price3)

    def weight4_formatted(self, obj):
        return "{0:.2f}".format(obj.weight4)

    def price4_formatted(self, obj):
        return "{0:.2f}".format(obj.price4)

    def weight5_formatted(self, obj):
        return "{0:.2f}".format(obj.weight5)

    def price5_formatted(self, obj):
        return "{0:.2f}".format(obj.price5)

    weight1_formatted.short_description = "wgt"
    price1_formatted.short_description = "px"

    weight2_formatted.short_description = "wgt"
    price2_formatted.short_description = "px"

    weight3_formatted.short_description = "wgt"
    price3_formatted.short_description = "px"

    weight4_formatted.short_description = "wgt"
    price4_formatted.short_description = "px"

    weight5_formatted.short_description = "wgt"
    price5_formatted.short_description = "px"


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Sale, SaleAdmin)

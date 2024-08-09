from django.db import models
from datetime import date, datetime


class Auction(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    slug = models.SlugField(unique=True)
    full_name = models.CharField(max_length=250, unique=True)
    market = models.CharField(max_length=250)
    last_final_sale_date = models.DateField(default=date(2023, 1, 1))
    offset = models.IntegerField(default=0)
    mmn_url = models.CharField(max_length=500)

    class Meta:
        ordering = ["slug"]

    def __str__(self) -> str:
        return f"{self.name} ({self.slug})"


class Sale(models.Model):
    date = models.DateField()
    auction = models.ForeignKey(Auction, related_name="sales", on_delete=models.CASCADE)

    # 700 -749
    head1 = models.IntegerField(default=0, verbose_name="hd 700")
    weight1 = models.FloatField(default=0, verbose_name="wgt 700-749")
    price1 = models.FloatField(default=0, verbose_name="px 700-749")

    # 750 -799
    head2 = models.IntegerField(default=0, verbose_name="hd 750")
    weight2 = models.FloatField(default=0, verbose_name="wgt 750-799")
    price2 = models.FloatField(default=0, verbose_name="wgt 750-799")

    # 800 -849
    head3 = models.IntegerField(default=0, verbose_name="hd 800")
    weight3 = models.FloatField(default=0, verbose_name="wgt 800-849")
    price3 = models.FloatField(default=0, verbose_name="wgt 800-849")

    # 850 -899
    head4 = models.IntegerField(default=0, verbose_name="hd 850")
    weight4 = models.FloatField(default=0, verbose_name="wgt 850-899")
    price4 = models.FloatField(default=0, verbose_name="px 850-899")

    # 8TOTAL
    head5 = models.IntegerField(default=0, verbose_name="hd")
    weight5 = models.FloatField(default=0, verbose_name="wgt")
    price5 = models.FloatField(default=0, verbose_name="px")

    # ETC
    final_ind = models.CharField(max_length=25, default="final")
    region = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"{self.date}: {self.auction.name}"

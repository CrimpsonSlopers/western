from django.db import models
from datetime import datetime


class Auction(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    slug = models.SlugField(unique=True)
    full_name = models.CharField(max_length=250, unique=True)
    market = models.CharField(max_length=250)
    last_final_sale_date = models.DateField(default=datetime(2023, 1, 1))
    offset = models.IntegerField(default=0)
    mmn_url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.name} ({self.slug})"


class Sale(models.Model):
    date = models.DateField()
    auction = models.ForeignKey(Auction, related_name="sales", on_delete=models.CASCADE)
    head1 = models.IntegerField(default=0)
    weight1 = models.FloatField(default=0)
    price1 = models.FloatField(default=0)
    head2 = models.IntegerField(default=0)
    weight2 = models.FloatField(default=0)
    price2 = models.FloatField(default=0)
    head3 = models.IntegerField(default=0)
    weight3 = models.FloatField(default=0)
    price3 = models.FloatField(default=0)
    head4 = models.IntegerField(default=0)
    weight4 = models.FloatField(default=0)
    price4 = models.FloatField(default=0)
    head5 = models.IntegerField(default=0)
    weight5 = models.FloatField(default=0)
    price5 = models.FloatField(default=0)
    final_ind = models.CharField(max_length=25, default="final")
    region = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"{self.date}: {self.auction.name}"

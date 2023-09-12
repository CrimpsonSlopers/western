from django.urls import path
from .views import *

urlpatterns = [
    path("sale", SaleView.as_view()),
    path("sale/<int:id>", SaleView.as_view()),
    path("auction", AuctionView.as_view()),
    path("auction/<int:id>", AuctionView.as_view()),
    path("update/<int:slug>", UpdateView.as_view()),
]

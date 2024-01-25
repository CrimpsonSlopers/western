from django.urls import path
from .views import *

urlpatterns = [
    path("auction", AuctionView.as_view()),
    path("auction/<int:id>", AuctionView.as_view()),
    path("update/<int:slug>", UpdateView.as_view()),
    path("authenticate", UserPermissionCheckAPIView.as_view()),
    path("reports", ReportView.as_view()),
    # path("add", AddAuctionFromJSON.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('transaction/create', views.TransactionCreateView.as_view()),
    path('transaction', views.DayHoldingsView.as_view()),

]

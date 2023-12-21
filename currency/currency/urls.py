
from django.contrib import admin
from django.urls import path

from currencyapp.views import CurrencyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/currencylist/', CurrencyAPIView.as_view()),
]

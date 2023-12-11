from django.urls import path

from api.views import *

urlpatterns = [
    path("", main_view),
    path("sum/", sum_view),
]
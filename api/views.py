from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet


@api_view(["GET"])
def main_view(request):
    dt = datetime.now()
    return Response({"status": dt.weekday()})


@api_view(["GET"])
def sum_view(request):
    num1, num2 = int(request.GET['num1']), int(request.GET['num2'])
    return Response({"status": num1 + num2})

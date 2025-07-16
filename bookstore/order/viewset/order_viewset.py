from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializers

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializers
    queryset         = Order.objects.all().order_by('id')
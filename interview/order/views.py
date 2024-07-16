from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderListBetweenDatesView(APIView):
    serializer_class = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        startDateStr = kwargs['startDate']
        embargoDateStr = kwargs['embargoDate']
        queryset = Order.get_in_between_dates(startDateStr, embargoDateStr)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=200)

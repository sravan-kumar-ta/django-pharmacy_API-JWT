from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from medicines.models import Medicine
from .models import Order
from .serializers import MedicineSerializer, OrderSerializer
from django.db.models import Q


# Create your views here.
class MedicineList(ListCreateAPIView):
    serializer_class = MedicineSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Medicine.objects.filter(Q(stock__gt=0), is_active=True)


class OrderView(GenericAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderedList(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

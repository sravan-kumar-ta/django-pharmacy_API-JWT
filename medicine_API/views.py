from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from medicines.models import Medicine
from .serializers import MedicineSerializer
from django.db.models import Q


# Create your views here.
class MedicineList(ListCreateAPIView):
    serializer_class = MedicineSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Medicine.objects.filter(Q(stock__gt=0), is_active=True)

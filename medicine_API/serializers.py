from rest_framework.serializers import ModelSerializer
from medicines.models import Medicine


class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'title', 'category', 'image', 'manufactured_by', 'price', 'is_active', 'stock']

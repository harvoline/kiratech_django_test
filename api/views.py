from rest_framework import viewsets
from rest_framework import permissions
from inventory.models import Inventory, Supplier
from api.serializers import InventorySerializer, SupplierSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.all().order_by('id')

        if self.request.query_params.get('name'):
            queryset = queryset.filter(name__icontains=self.request.query_params.get('name'))

        return queryset


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = SupplierSerializer

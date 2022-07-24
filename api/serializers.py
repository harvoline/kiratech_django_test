from rest_framework import serializers
from inventory.models import Inventory, Supplier


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.ReadOnlyField(source='supplier.name')

    class Meta:
        model = Inventory
        fields = ('id', 'name', 'supplier_name', 'availability')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

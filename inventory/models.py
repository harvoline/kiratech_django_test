import json

from django.db import models

# Create your models here.


class Inventory(models.Model):
    # id - Sample in case you want to change id to another name. By default, PK is auto
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    note = models.TextField(null=True, blank=True)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        # print(self._meta.fields)
        # for i in self._meta.fields:
        #     print(i.name)
        #     print(getattr(self, i.name))
        #     # print(self.get__attribute__(i))
        # model_json = {field.name:getattr(self, field.name) for field in self._meta.fields}
        # return json.dumps({field.name:getattr(self, field.name) for field in self._meta.fields})
        return self.name


class Supplier(models.Model):
    # id - Sample in case you want to change id to another name. By default, PK is auto
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        # return json.dumps({
        #     "id": self.id,
        #     "name": self.name,
        # })
        return self.name


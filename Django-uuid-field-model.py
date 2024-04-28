from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

###################################### Categories ###########################
class AssetCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name  = "Asset Category"
        verbose_name_plural = "Asset Catatories"

###################################### Asset Location ###########################
        
class AssetLocation(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name  = "Asset Location"
        verbose_name_plural = "Asset Locations"

###################################### Asset Vendor ###########################

class Vendor(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name  = "Asset Vonder"
        verbose_name_plural = "Asset Vonders"

###################################### Assets ###########################

class Asset(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    asset_id = models.CharField(max_length=36, default=uuid4)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(AssetLocation, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    vender = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    purchased = models.BooleanField(default=True)
    puchased_date = models.DateTimeField(auto_now=True)
    doner = models.CharField(max_length=30, blank=True, null=True)
    is_expired = models.BooleanField(default=False)
    expired_date = models.DateField(blank=True, null=True)
    # tag number 
    capital = models.BooleanField(default=False) # under 100 - 5000 $ and small 
    is_active = models.BooleanField(default=True)  # For monitoring asset status
    # Add more fields as needed

    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name  = "Asset"
        verbose_name_plural = "Assets"

###################################### Assignments to employees ###########################

class UserAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)
    delivery_from = models.ForeignKey(AssetLocation, on_delete=models.SET_NULL, blank=True, null=True)
    return_date = models.DateField(null=True, blank=True)
    # Add more fields as needed

    def __str__(self) -> str:
        return f"{self.asset.name} -- {self.user.first_name + self.user.last_name}"
    
    class Meta: 
        verbose_name  = "Asset Asignment"
        verbose_name_plural = "Asset Asignments"


###################################### Assignments to employees ###########################

class Stock(models.Model):
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    # Add more fields as needed

    def __str__(self) -> str:
        return f"{self.asset.name} - {self.quantity} - {self.status}"
    
    class Meta:
        verbose_name  = "Stock"
        verbose_name_plural = "Stock"

###################################### Assignments to employees ###########################

class MaintenanceActivity(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    # Add more fields as needed

    def __str__(self) -> str:
        return self.asset.name + self.date

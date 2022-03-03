import uuid
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default = uuid.uuid4,
            editable=False
    )
    username = models.CharField(max_length=30)

class CustomerContacts(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = PhoneNumberField()

class CustomerDetails(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contacts = models.ForeignKey(CustomerContacts, on_delete=models.PROTECT)
    credits = models.IntegerField(default=0)
    created = models.DateField(default=datetime.now())

@receiver(post_save, sender=Customer)
def create_customers_details(sender, instance, created, **kargs):
    contacts = CustomerContacts.objects.create(
        customer=instance
    )
    details = CustomerDetails.objects.create(
        customer=instance,
        contacts=contacts
    )
    contacts.save()
    details.save()


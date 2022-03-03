from rest_framework import serializers
from datetime import datetime
from .models import Customer, CustomerContacts, CustomerDetails

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            'username'
        ]

class CustomerListSerializer(serializers.Serializer):

    class Meta:
        customers = CustomerSerializer(many=True)

class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            'username'
        ]

class CustomerDetailsSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()
    contacts = ContactsSerializer()

    class Meta:
        model = CustomerContacts
        fields = [
            'credits',
            'created'
        ]


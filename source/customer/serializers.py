from rest_framework import serializers
from datetime import datetime
from .models import Customer, CustomerContacts, CustomerDetails

class CustomerSerializer(serializers.ModelSerializer):
    ''' This is the base customer serializer for one customer
    '''

    class Meta:
        model = Customer
        fields = [
            'id',
            'username'
        ]

class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerContacts
        fields = [
            'phone'
        ]

class CustomerDetailsSerializer(serializers.ModelSerializer):
    ''' This is the details customer serializer for one customer
    '''

    customer = CustomerSerializer()
    contacts = ContactsSerializer()

    class Meta:
        model = CustomerDetails
        fields = [
            'customer',
            'contacts',
            'credits',
            'created'
        ]


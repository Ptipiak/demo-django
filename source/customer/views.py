from rest_framework import authentication, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Customer, CustomerDetails
from .serializers import CustomerSerializer, CustomerDetailsSerializer

# This is the Customers base view, allow you to 
# get data on present customers, as well as some details
# and set the customers data.
class CustomersView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [authentication.TokenAuthentication]

    # In order to serialize multiples objects, you need to pass
    # many=True on to the serializer arugments
    def list(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(data=customers, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    # This create a customer
    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        serializer.create(serializer.data)
        return Response(status=status.HTTP_201_CREATED)

    # This should get the CustomerDetails of the queried customer id
    @action(methods=['post','get'], detail=True, url_path='get-details', url_name='details')
    def get_details(self, request, pk=None):
        customer = Customer.objects.get(id=pk)
        customer_details = CustomerDetails.objects.get(customer__id = customer.id)
        serializer = CustomerDetailsSerializer(customer_details)
        data = serializer.data
        return Response(data)


from rest_framework import authentication, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Customer, CustomerDetails
from .serializers import CustomerSerializer, CustomerDetailsSerializer

# Create your views here.
class CustomersView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def list(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(data=customers, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        serializer.create(serializer.data).save()
        return Response(serializer.data)

    @action(methods=['post','get'], detail=True, url_path='get-details', url_name='details')
    def get_details(self, request, pk=None):
        customer = Customer.objects.get(id=pk)
        customer_details = CustomerDetails.objects.get(customer = customer.id)
        serializer = CustomerDetailsSerializer(customer_details)
        data = serializer.data
        return Response(data)


from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Item, administration, student
from .serializers import ItemSerializer, StudentSerializer, AdministrationSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, world!"})


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Function-based view for retrieving all items
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# CRUD views for Item model
class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# CRUD views for student model
class StudentCreateView(generics.CreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

# CRUD views for administration model
class AdministrationCreateView(generics.CreateAPIView):
    queryset = administration.objects.all()
    serializer_class = AdministrationSerializer

class AdministrationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = administration.objects.all()
    serializer_class = AdministrationSerializer

#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Userstable, Businesscategorytable, Businessestable, Itemtable, Interestitemtable, Managertable, Messagestable, Typeoftreatmenttable, Requesttable, Ridetable
from .serializers import UsersSerializer, BusinesscategorySerializer, BusinessesSerializer, ItemSerializer, InterestitemSerializer, ManagerSerializer, MessagesSerializer, TypeoftreatmentSerializer, RequestSerializer, RideSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Userstable.objects.all()
    serializer_class = UsersSerializer

class BusinessCategoryViewSet(viewsets.ModelViewSet):
    queryset = Businesscategorytable.objects.all()
    serializer_class = BusinesscategorySerializer

class BusinessesViewSet(viewsets.ModelViewSet):
    queryset = Businessestable.objects.all()
    serializer_class = BusinessesSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Itemtable.objects.all()
    serializer_class = ItemSerializer

class InterestItemViewSet(viewsets.ModelViewSet):
    queryset = Interestitemtable.objects.all()
    serializer_class = InterestitemSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Managertable.objects.all()
    serializer_class = ManagerSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messagestable.objects.all()
    serializer_class = MessagesSerializer

class TypeOfTreatmentViewSet(viewsets.ModelViewSet):
    queryset = Typeoftreatmenttable.objects.all()
    serializer_class = TypeoftreatmentSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Requesttable.objects.all()
    serializer_class = RequestSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ridetable.objects.all()
    serializer_class = RideSerializer
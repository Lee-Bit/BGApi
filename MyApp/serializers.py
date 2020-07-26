from rest_framework import serializers 
from .models import Userstable, Businesscategorytable, Businessestable, Itemtable, Interestitemtable, Managertable, Messagestable, Typeoftreatmenttable, Requesttable, Ridetable
 
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userstable
        fields = ['firstname','lastname', 'phone', 'password', 'housenumber', 'email', 'location', 'photo', 'apartmentnumber', 'street']

class BusinesscategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Businesscategorytable
        fields =['name', 'icon']

class BusinessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessestable
        fields = ['name', 'phone', 'category', 'details', 'address', 'photo']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemtable
        fields = ['id', 'type', 'price', 'publishdate', 'publisher']

class InterestitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interestitemtable
        fields = ['interest_item_table_id', 'item_id', 'interestuser', 'state']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managertable
        fields = ['phone']

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagestable
        fields =['id', 'title', 'cont', 'date', 'time', 'publisher']

class TypeoftreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeoftreatmenttable
        fields = ['type', 'manager']

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requesttable
        fields = ['typeoftreatment', 'publisher', 'id', 'state', 'cont', 'publishdate', 'publishtime', 'finishdate', 'finishtime']

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ridetable
        fields = ['ride_table_id', 'passenger', 'optionaldriver', 'radius', 'date', 'time']
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from .permissions import *

#ModelViewSet = All-in-One CRUD class

class ProductViewSet(ModelViewSet):#Simple CRUD operation with ModelViewSet
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   # permission_classes = [IsAuthenticated]   #jwt 
    
    
    def get_permissions(self): #only view list in user role
        if self.action in ['list','retrieve']:#get,id_get
            permission_classes = [IsAuthenticated] #jwt
        else:
            permission_classes = [IsAdmin] #add,up,del =Admin
            
        return [p() for p in permission_classes]#append kar





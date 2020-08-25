from django.urls import path, include 
from rest_framework import routers
from MyApp import views


router = routers.DefaultRouter()
router.register(r'Users', views.UsersViewSet)
router.register(r'BusinessCatego', views.BusinessCategoryViewSet)
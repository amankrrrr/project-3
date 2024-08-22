from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Index.as_view(template_name='index.html'), name='index'),
    path('login', CustomLoginView.as_view(template_name='login.html'), name='login'),
    
    path('InventoryList', InventoryList.as_view(template_name='InventoryList.html'), name='InventoryList'),
    
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    
    path('InventoryAdd', InventoryAdd.as_view(template_name='InventoryAdd.html'), name='InventoryAdd'),
    
    
    path('register', RegisterPage.as_view(template_name='register.html'), name='register'),
    
    
    path('InventoryDetail/<int:pk>', InventoryDetail.as_view(template_name='InventoryDetail.html'), name='InventoryDetail'),
    
    path('InventoryDelete/<int:pk>', InventoryDelete.as_view(template_name='InventoryDelete.html'), name='InventoryDelete'),
    
    path('InventoryUpdate/<int:pk>', InventoryUpdate.as_view(template_name='InventoryUpdate.html'), name='InventoryUpdate'),
]

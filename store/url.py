from django.urls import path
from . views import *

urlpatterns = [
    path('store/',index,name='index'),
    path('products/<int:pk>/',detail,name='detail'),
    path('sell',sell,name='sell'),
    path('Phone/',phone,name='cat')
]

from  django.urls import path
from .views import *

urlpatterns= [
    path('get/<int:pk>', rTest),
    path('post/<int:pk>', sTest),
    path('result/<int:pk>', retrieveResult),
]
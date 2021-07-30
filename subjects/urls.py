from  django.urls import path
from .views import *

urlpatterns= [
    path('create', cSubject),
    path('delete', dSubject),

    path('q_create', cQuestion),
    path('q_delete', dQuestion),

]
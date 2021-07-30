from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('students.urls')),
    path('subject/', include('subjects.urls')),
    path('test/', include('tests.urls')),
]

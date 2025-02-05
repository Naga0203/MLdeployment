from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('' , include('HDmodel.urls')),
    path('admin/', admin.site.urls),    
]

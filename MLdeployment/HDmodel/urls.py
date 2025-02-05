from django.urls import path
from .views import get_predictions, pred

urlpatterns = [
    path('', pred, name='home'),  
    path('result', get_predictions, name='result'),
]

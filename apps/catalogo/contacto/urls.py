from django.urls import path
from .views import ContactoAPIView, ContactoDetails

app_name = 'contacto'

urlpatterns = [
    path('', ContactoAPIView.as_view(), name='contacto'),
    path('<int:pk>/', ContactoDetails.as_view()),
]
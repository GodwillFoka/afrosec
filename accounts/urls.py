from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.PreRegisterView.as_view(), name='preregister'),
    path('inscription/merci/', views.PreRegisterSuccessView.as_view(), name='preregister_success'),
]

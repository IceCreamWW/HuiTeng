from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('certificate/<int:certificate_id>/', views.certificate, name='certificate'),
]
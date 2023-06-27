from django.urls import path
from sproj import views

urlpatterns = [
    path('', views.mysproj)
]

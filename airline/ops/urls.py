from django.urls import path
from . import views


urlpatterns = [
    path('ops/', views.dashboard, name='ops_dashboard'),
]

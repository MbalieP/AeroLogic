from django.urls import path
from . import views


urlpatterns = [
    path('flight/<int:flight_id>/checkin', views.checkin_view, name='checkin'),
]

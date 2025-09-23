from django.shortcuts import render
from flights.models import Flight


def dashboard(request):
    flights = Flight.objects.all().order_by('id')[:20]
    return render(request, 'ops/dashboard.html', {
        'flights': flights
    })

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from flights.models import Flight, Passenger
from .models import BoardingPass


def checkin_view(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        passenger_id = int(request.POST.get('passenger'))
        passenger = get_object_or_404(Passenger, pk=passenger_id)
        bp, created = BoardingPass.objects.get_or_create(
            flight=flight,
            passenger=passenger,
            defaults={
                'checked_in_at': timezone.now()
            }
        )
        if not created and bp.checked_in_at is None:
            bp.checked_in_at = timezone.now()
            bp.save()
        messages.success(request, f"Checked in {passenger} for flight {flight.id}.")
        return redirect('checkin', flight_id=flight.id)
    checked_in = BoardingPass.objects.filter(flight=flight).select_related('passenger')
    eligible = Passenger.objects.filter(flights=flight).exclude(boarding_passes__flight=flight)
    return render(request, 'checkin/checkin.html', {
        'flight': flight,
        'checked_in': checked_in,
        'eligible': eligible
    })

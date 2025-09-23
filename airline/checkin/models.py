from django.db import models
from flights.models import Flight, Passenger


class BoardingPass(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='boarding_passes')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='boarding_passes')
    seat_code = models.CharField(max_length=5, blank=True)
    qr_code_data = models.CharField(max_length=256, blank=True)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('flight', 'passenger')

    def __str__(self):
        return f"BP {self.flight_id}-{self.passenger_id} {self.seat_code}"

from django.db import models
from flights.models import Flight, Passenger


class IrOpsEvent(models.Model):
    TYPE_CHOICES = (
        ('CANCEL', 'Cancellation'),
        ('DELAY', 'Delay'),
    )
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='irops_events')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    reason = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_display()} for flight {self.flight_id}" 


class ReaccommodationSuggestion(models.Model):
    from_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reaccom_from')
    to_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reaccom_to')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='reaccom_suggestions')
    score = models.FloatField(default=0)
    status = models.CharField(max_length=16, default='PENDING')

    def __str__(self):
        return f"P{self.passenger_id} {self.from_flight_id}->{self.to_flight_id} ({self.score})"

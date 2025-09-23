from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"


class Aircraft(models.Model):
    type = models.CharField(max_length=64)
    range_nm = models.IntegerField(default=0)
    seat_layout = models.CharField(max_length=32, help_text="e.g., 3-3 or custom layout code")

    def __str__(self):
        return f"{self.type}"


class Seat(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='seats')
    row = models.IntegerField()
    letter = models.CharField(max_length=1)
    cabin = models.CharField(max_length=16, default='MAIN')

    class Meta:
        unique_together = ('aircraft', 'row', 'letter')

    def __str__(self):
        return f"{self.row}{self.letter} ({self.aircraft})"


class SeatAssignment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='seat_assignments')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='seat_assignments')
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT, related_name='assignments')
    status = models.CharField(max_length=16, default='CONFIRMED')

    class Meta:
        unique_together = ('flight', 'seat')

    def __str__(self):
        return f"F{self.flight_id} {self.seat} -> {self.passenger}"
    
from django.core.management.base import BaseCommand
from flights.models import Airport, Flight, Passenger


class Command(BaseCommand):
    help = 'Seed demo data: airports, one flight, and passengers.'

    def handle(self, *args, **options):
        jfk, _ = Airport.objects.get_or_create(code='JFK', defaults={'city': 'New York'})
        lax, _ = Airport.objects.get_or_create(code='LAX', defaults={'city': 'Los Angeles'})

        flight, _ = Flight.objects.get_or_create(
            origin=jfk, destination=lax, defaults={'duration': 360}
        )

        passengers = [
            ('Alice', 'Anderson'),
            ('Bob', 'Brown'),
            ('Charlie', 'Clark'),
        ]
        created = 0
        for first, last in passengers:
            p, _ = Passenger.objects.get_or_create(first=first, last=last)
            p.flights.add(flight)
            created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Seeded: Airports(JFK,LAX), Flight {flight.id}, Passengers added to flight: {created}"))

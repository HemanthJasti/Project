from django.db import models
from django.utils import timezone

class TravelPlan(models.Model):
    DEPARTURE_DATE = 'departure_date'
    ARRIVAL_DATE = 'arrival_date'
    STATUS_CHOICES = [
        (DEPARTURE_DATE, 'Departure date'),
        (ARRIVAL_DATE, 'Arrival date'),
    ]

    departure_date = models.DateField()
    arrival_date = models.DateField()
    travel_cost = models.DecimalField(max_digits=8, decimal_places=2)
    distance = models.PositiveIntegerField()
    description = models.TextField()
    approval = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=DEPARTURE_DATE,
    )

    def __str__(self):
        return f'Travel Plan #{self.pk}: {self.departure_date} - {self.arrival_date}'

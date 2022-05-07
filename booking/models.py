from django.db import models
from conference.models import Conference


class ConferenceBooking(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    date_field = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()

    def __str__(self):
        return f'{self.date_field} {self.time_from} - {self.time_to}  {self.department} '

from django.db import models
from timezone_utils.choices import ALL_TIMEZONES_CHOICES
import pytz

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=150,choices=ALL_TIMEZONES_CHOICES) 

    def __str__(self):
        return self.id+"-"+self.real_name+"-"+self.tz

class Activity(models.Model):
    member = models.ForeignKey(Member, related_name="activity_periods", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.start_time)+"--"+str(self.end_time)
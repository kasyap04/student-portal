from django.db import models

# Create your models here.


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    date = models.DateField()
    body = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'events'

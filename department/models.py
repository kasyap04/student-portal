from django.db import models

# Create your models here.


class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=6)
    duration = models.CharField(max_length=2)
    hod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'department'

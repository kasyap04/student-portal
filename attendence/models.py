from django.db import models

# Create your models here.
class Attendence(models.Model):
    attend_id = models.AutoField(primary_key=True)
    stu_id = models.IntegerField()
    dep_id = models.IntegerField()
    sem = models.CharField(max_length=5)
    date = models.DateField()
    attend = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'attendence'
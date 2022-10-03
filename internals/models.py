from django.db import models

# Create your models here.


class Internals(models.Model):
    int_id = models.AutoField(primary_key=True)
    dep_id = models.IntegerField()
    sem = models.CharField(max_length=5)
    sub_id = models.IntegerField()
    stu_id = models.IntegerField()
    obtained_mark = models.CharField(max_length=3)
    total_mark = models.CharField(max_length=3)
    exam_name = models.CharField(max_length=75)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'internals'

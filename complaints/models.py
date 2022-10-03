from django.db import models

# Create your models here.


class Complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    stu_id = models.IntegerField()
    to = models.CharField(max_length=10)
    to_id = models.IntegerField()
    body = models.CharField(max_length=200)
    date = models.DateTimeField()
    respond_date = models.DateTimeField(blank=True, null=True)
    reply = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaints'

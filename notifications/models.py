from django.db import models

# Create your models here.

class Notification(models.Model):
    notif_id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=100)
    send_by = models.CharField(max_length=10)
    send_id = models.IntegerField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notification'





class NotifConnect(models.Model):
    connnect_id = models.AutoField(primary_key=True)
    notif_id = models.IntegerField()
    stu_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notif_connect'


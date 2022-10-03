from django.db import models

# Create your models here.


class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    login_key = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10)
    u_id = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Master(models.Model):
    master_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    number = models.IntegerField()
    post = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'master'

from django.db import models

# Create your models here.

class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    adm_no = models.CharField(max_length=12)
    name = models.CharField(max_length=25)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    phone = models.CharField(max_length=15)
    join_year = models.DateField()
    dep_id = models.IntegerField()
    current_sem = models.CharField(max_length=5)
    email = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    passout = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


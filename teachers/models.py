from django.db import models

# Create your models here.


class Teachers(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    qualification = models.CharField(max_length=25)
    experiance = models.CharField(max_length=25)
    dep_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teachers'




class ClassTeacher(models.Model):
    ct_id = models.AutoField(primary_key=True)
    dep_id = models.IntegerField()
    sem = models.IntegerField()
    teacher_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_teacher'



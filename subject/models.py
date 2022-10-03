from django.db import models

# Create your models here.


class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    dep_id = models.IntegerField()
    sem = models.CharField(max_length=5)
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)
    teacher_id = models.IntegerField()
    adm_year = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'subject'

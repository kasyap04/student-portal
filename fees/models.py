from django.db import models

# Create your models here.


class Fees(models.Model):
    fee_id = models.AutoField(primary_key=True)
    dep_id = models.IntegerField()
    sem = models.IntegerField()
    fee_name = models.CharField(max_length=25)
    fee_amount = models.CharField(max_length=5)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees'


class FeePaid(models.Model):
    paid_id = models.AutoField(primary_key=True)
    stu_id = models.IntegerField()
    fee_id = models.IntegerField()
    amount = models.CharField(max_length=6)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'fee_paid'

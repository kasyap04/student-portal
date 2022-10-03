from django.db import models

# Create your models here.


class Classroom(models.Model):
    classroom_id = models.AutoField(primary_key=True)
    # dep_id = models.IntegerField()
    # sem = models.IntegerField()
    sub_id = models.IntegerField()
    context = models.CharField(max_length=10)
    context_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'classroom'



class Classwork(models.Model):
    work_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    body = models.TextField()
    date = models.DateField()
    due_date = models.DateField(blank=True, null=True)
    due_time = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classwork'




class UserShare(models.Model):
    share_id = models.AutoField(primary_key=True)
    body = models.TextField()
    date = models.DateField()
    send_user = models.CharField(max_length=10)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_share'




class ClassMedia(models.Model):
    media_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    context = models.CharField(max_length=10)
    context_id = models.IntegerField()
    shareby = models.CharField(max_length=10)
    shareby_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_media'


class Submited(models.Model):
    submit_id = models.AutoField(primary_key=True)
    work_id = models.IntegerField()
    stu_id = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'submited'


from django.db import models


class Item(models.Model):
    name=models.CharField(max_length=100)
    Created= models.DateTimeField(auto_now_add=True)

class student(models.Model):
    fname= models.CharField(max_length=100)
    sname=models.CharField(max_length=100)
    age=models.IntegerField()


class administration (models.Model):

    id_no=models.IntegerField()
    admin_name=models.CharField(max_length=100)
    















from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Facility(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
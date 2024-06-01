from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    complaint = models.TextField()
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='complaint_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.email
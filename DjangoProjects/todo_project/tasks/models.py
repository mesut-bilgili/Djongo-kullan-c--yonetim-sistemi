from django.db import models

# Create your models here.
class Person (models.Model):
    first_name=models .CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    tc_number=models.CharField(max_length=11,unique=True)
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    note=models.TextField(blank=True)
    photo=models.ImageField(upload_to="photos/")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


 
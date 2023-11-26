from datetime import date, datetime

from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField










class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    third_name=models.CharField(max_length=20)
    address=models.CharField(max_length=100,blank=True)
    puplished_at=models.DateTimeField(auto_now=True   )


    def __str__(self):
        return self.user.username

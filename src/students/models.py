from django.contrib.auth.models import User
from django.db import models
from accounts.models import UserProfile

#from accounts.models import UserProfile


# Create your models here.
NUMBER_OF_JUZE_CHOICES = (
    ("0", "-"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
    ("30", "30"),
    ("31", "30 مع التجويد"),
)

class Student_Apply(models.Model):
    basic_info=models.OneToOneField(UserProfile,on_delete=models.CASCADE)#include username,passward,fname,sname,thrname,email
    full_name = models.CharField(max_length=255, blank=True)
    student_shekh_mohafez=models.ForeignKey('Shekh_Mohafez',on_delete=models.CASCADE)
    student_shekh_tester=models.ForeignKey('Shekh_Tester',on_delete=models.CASCADE)
    student_country=models.ForeignKey('Country',on_delete=models.CASCADE)
    number_of_Juze=models.CharField( max_length = 20, choices = NUMBER_OF_JUZE_CHOICES)
    national_id=models.DecimalField(max_digits=14,decimal_places=0,null=False,unique=True)
    phone_number1 = models.CharField(max_length=15, unique=True ,blank=True, null=True, help_text="Enter phone number without country code")
    phone_number2 =  models.CharField(max_length=15, unique=True ,blank=True, null=True, help_text="Enter phone number without country code")
    result=models.DecimalField(max_digits=3,decimal_places=2,blank=True, null=True)
    current_date = models.DateField(auto_now=True)
    #print('5555555555',UserProfile.objects.get(pk=User.pk))
    def save(self, *args, **kwargs):
        # Automatically update the full name when saving
        # Automatically update the full name during creation or update
        if not self.full_name:
            self.full_name = f"{self.basic_info.user.first_name} {self.basic_info.user.last_name} {self.basic_info.third_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.basic_info.user.username



class Shekh_Mohafez(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number =  models.CharField(max_length=15, unique=True ,blank=True, null=True, help_text="Enter phone number without country code")

    def __str__(self):
        return self.user.username
class Shekh_Tester(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number =  models.CharField(max_length=15, unique=True ,blank=True, null=True, help_text="Enter phone number without country code")
    def __str__(self):
        return self.user.username

class Country(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
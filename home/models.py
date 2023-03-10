import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from home.valiidators import validate_file_size


# Create your models here.
class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='student',primary_key=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone = models.IntegerField()
    image = models.FileField(upload_to='image',validators=[validate_file_size])
    approval_status = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def age(self):
        age = datetime.date.today() - self.date_of_birth
        return int((age).days / 365.25)

class Admin(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone = models.IntegerField()
    # photo = models.ImageField(upload_to='image', default=0)

    def __str__(self):
        return self.name

class Marks(models.Model):
    name = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    english = models.IntegerField(validators=[MaxValueValidator(100)])
    maths = models.IntegerField(validators=[MaxValueValidator(100)])
    hindi = models.IntegerField(validators=[MaxValueValidator(100)]
                                )
    science = models.IntegerField(validators=[MaxValueValidator(100)])
    malayalam = models.IntegerField(validators=[MaxValueValidator(100)])

    total = models.IntegerField(default= 0)

    def __str__(self):
        return self.name + self.total

    def total(self):
        self.total = self.english + self.maths + self.hindi + self.science + self.malayalam
        return self.total

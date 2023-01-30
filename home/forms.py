from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.core.validators import RegexValidator

from home.models import Student, Login_view, Admin, Marks


class DateInput(forms.DateInput):
    input_type = 'date'



class userregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,validators=[
        RegexValidator(regex='^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.* ).{8,}$', message='Please enter a Valid password')])
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class studentform(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = Student
        exclude = ("user","approval_status",)

def clean(self):
    width, height = get_image_dimensions(self.cleaned_data.get('image'))
    if width < 1300 or height < 400:
        raise forms.ValidationError("Image dimensions is too small, minimum is 1300x400")
        return cleaned_data

class adminform(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput)
    class Meta:
        model = Admin
        exclude = ("user",)

class marksform(forms.ModelForm):
    class Meta:
        model = Marks
        fields = "__all__"

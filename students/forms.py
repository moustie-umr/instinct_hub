from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from courses.models import Course

""" create the functionality for students
to enroll in courses """

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)


#Extend default User model

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Last Name')
    email = forms.EmailField(max_length=254, help_text='Required. Fill a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

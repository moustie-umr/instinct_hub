from django import forms
from courses.models import Course

""" create the functionality for students
to enroll in courses """

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)

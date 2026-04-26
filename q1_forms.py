
from django import forms
from Q1.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'contact', 'email']
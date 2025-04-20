from django import forms
from .models import student, subject, result

class studentform(forms.ModelForm):
    
    class Meta:
        model = student
        fields = ("name",)

class subjectForm(forms.ModelForm):
    
    class Meta:
        model = subject
        fields = ("name",)

class resultForm(forms.ModelForm):
    
    class Meta:
        model = result
        fields = ("student", "subject", "marks")

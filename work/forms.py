from django import forms
from work.models import User,Taskmodel


class Register(forms.ModelForm):

    class Meta:

        model=User
        fields=['username','first_name',"last_name","email","password"]


class LoginForm(forms.Form):
   username=forms.CharField()
   password=forms.CharField()



class TaskForm(forms.ModelForm):

    class Meta:

        model=Taskmodel
        fields=['task_name','task_description']
        widgets={
            'task_name': forms.TextInput(attrs={'class':'form_control','placeholder': 'enter the task'}),
            'task_description': forms.Textarea(attrs={'class':'form-control','column':20,'rows':5, 'placeholder': 'enter a description'})
        }


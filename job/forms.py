from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactModel
from .models import upload

class ContactForm(forms.ModelForm):
	class Meta:
		model=ContactModel
		fields=['name','email','message']


class uploadForm(forms.ModelForm):
    class Meta:
        model=upload
        fields=['name','email','address','file']



	


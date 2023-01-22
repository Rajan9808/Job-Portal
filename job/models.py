from django.db import models

# Create your models here.
class ContactModel(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(max_length=50)
	message=models.CharField(max_length=300)

	def __str__(self):
		return self.name



class upload(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=30)
	address=models.CharField(max_length=50)
	file=models.FileField(upload_to="media/new/",max_length=250, null=True) # for creating file input



	def __all__(self):
		return self





    



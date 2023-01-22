from django.contrib import admin
from .models import ContactModel
from .models import upload
# Register your models here.
admin.site.register(ContactModel)
admin.site.register(upload)
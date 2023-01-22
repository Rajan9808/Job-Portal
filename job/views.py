from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import ContactModel
from .forms import ContactForm
from .models import upload
from .forms import uploadForm

# Create your views here.
def IndexView(request):
	return render(request,'index.html')
	
def Signupview(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Already Exists !')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Already Exists !')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
				user.save()
				print('User created')
				return redirect('login')
		else:
			messages.info(request,'Password does not match !')
			return redirect('register')

	else:
		return render(request,'register.html')
	
	
	
def LoginView(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'Invalid Username / Password !')
			#return redirect('login')
	else:
		return render(request,'login.html')

	
	

def JobView(request):
	return render(request, 'job.html')



def ContactView(request):
	if request.method =="POST":
	     form=ContactForm(request.POST)
	     if form.is_valid():
		     name=form.cleaned_data['name']
		     email=form.cleaned_data['email']
		     message=form.cleaned_data['message']

		     data=ContactModel(name=name,email=email,message=message)
		     data.save()
	else:
		form = ContactForm()



	return render(request,'contact.html',{'form':form})
	#return render(request,'contact.html')



def Upload(request):
	if request.method == 'POST':
		form=uploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('upload')

	else:
		form=uploadForm()
		return render(request, 'upload.html',{'form':form})
    
   
        
    




   





# def indexx(request):
#     if request.method == 'POST':
#         form=indexForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')

#     else:
#         form = indexForm()
#     return render(request, 'index.html',{'form':form})



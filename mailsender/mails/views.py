from django.shortcuts import render,redirect
from mailsender.settings import EMAIL_HOST_USER
from .forms import EmailForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_page(request):
    context={}
    if request.method=="GET":
        return render(request,'login.html')
    else:

        u=request.POST['uname']
        p=request.POST['upass']
        
        u=authenticate(username=u,password=p)
        print(u)
        if not u == None:
            login(request,u)
            return redirect('home')
        else:
            dt={'success':True}
            return render(request,'login.html',dt)

def register_page(request):
    context={}
    if request.method=="GET":
        return render(request,'register.html')
    else:
   
        e=request.POST['email']
        u=request.POST['username']
        p=request.POST['password']
        if u=="" or p=="" or e=="":
            context['err']="Field cannot be blank"
            return render(request,'register.html',context)
        obj=User.objects.create(email=e,username=u)
        obj.set_password(p)
        obj.save()
        dt={'success':True}
        return render(request,'register.html',dt)

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        to_email = request.POST.get('to')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        sender_email = EMAIL_HOST_USER  
        send_mail(subject, description, sender_email, [to_email], fail_silently=False)
        Mail.objects.create(receipant=to_email, subject=subject, desc=description)
        return render(request, 'home.html')

    return render(request, 'home.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
def mails(request):
    obj =Mail.objects.all()
    dt={'data':obj}
    return render(request,'mails.html',dt)
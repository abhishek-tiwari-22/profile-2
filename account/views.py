from django.shortcuts import render,redirect
from django.http import Http404
from .models import *
from django.contrib import messages


def signin(request):

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        request.session.modified=True
        request.session['email']=email

        user=Details(email=email,password=password)

        if Details.objects.filter(email=email,password=password).exists():
            Details.objects.get(email=email,password=password)
            return redirect('/profile')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')

    return render(request, 'account/signin.html')


def signup(request):

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        dob=request.POST['dob']
        phone=request.POST['phone']

        dob=str(dob)
        dob=dob-',midnight'

        if password1==password2:
            if Details.objects.filter(email=email).exists():
                messages.info(request, "Email Already in use")
                return redirect('/signup')
            user=Details.objects.create(
                name=name,password=password1,email=email,dob=dob,phone=phone
            )
            user.save()
            return redirect('/')
        else:
            messages.info(request, "Both Passwords did not match")
            return redirect('/signup')
    else:
        return render(request, 'account/signup.html')

def profile(request):
    mail=request.session['email']
    user=Details.objects.get(email=mail)
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return render(request, 'account/http404.html')
    return render(request,'account/profile.html',{'user':user})

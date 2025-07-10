from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

def registration(request):
    EUMFO=UserForm()
    EPMFO=ProfileForm()
    d={'EUMFO':EUMFO,'EPMFO':EPMFO}

    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            #Done with User model 

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('Registration',
                      'Ur registration is Successfull',
                      'amudalabhanuteja5@gmail.com',
                      [MUFDO.email],
                      fail_silently=False)
            return HttpResponse('registration is Successfull')
        












    return render(request,'registration.html',d)
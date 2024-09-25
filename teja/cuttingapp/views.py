from django.shortcuts import render

from django.contrib.auth import authenticate,login

from django.shortcuts import redirect


from .forms import *


from .models import *


from django.core.mail import send_mail
# Create your views here.

def login_view(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=authenticate(username=username,password=password)
        if user is not None:
           login(request,user)
           return redirect('main')
        else:
           return redirect('login')  
    return render(request,'login.html')



def main_view(request):
         user=request.user
         if request.method == 'POST':
               name=request.POST['name']
               email1=request.POST['email_address']
               phoneno=request.POST['phone']
               category=request.POST['category']
               date=request.POST['date']
               message=request.POST['message']
               model=appointmentmodel(name=name,email=email1,phoneno=phoneno,category=category,date=date,message=message)
               email(name,email1,phoneno,category,message)
               model.save()
               return redirect ('main')
         return render(request,'main.html')


# def main_view(request):
#          form=appointmentform()
#          if request.method=='POST':
#               form=appointmentform(request.method)
#               if form.is_valid:
#                    form.save()
#          context={'form':form}
#          return render(request,'main.html',context)
 


def view(request):
     appointments=appointmentmodel.objects.all()
     return render(request,'view.html',{'appointments':appointments})


def email(name,email,phoneno,category,data):

    send_mail(
        f'Client:{name}',
        f'Mail Id:{email}\n'
        f'Phoneno:{phoneno}\n'
        f'Category:{category}\n'
        f'Message:{data}\n',
        'vivo80106@gmail.com',
        ['tirumalateja04@gmail.com'],
        fail_silently=False,
    )




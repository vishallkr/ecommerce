from django.shortcuts import render, redirect
from .models import user,prd


# Create your views here.

def log(request):
    return render(request, 'login.html')


def reg(request):
    return render(request, 'registration.html')


def home(request):
    data = prd.objects.all()
    for i in data:
        print(i.prd_name)
    return render(request, 'home.html',{'data':data})


def login_btn(request):
    print(">>>>>>>>>>>")
    if request.method == "POST":
        name = request.POST.get('name')
    pas = request.POST.get('pass')
    print(name)
    print(pas)
    if user.objects.filter(name=name, password=pas).exists():
        return redirect('home')
    else:
        return redirect('login')

    return render(request, 'login.html')


def reg_btn(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pas = request.POST.get('password')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        address = request.POST.get('address')

        print(name)
        print(pas)
        print(email)
        print(phoneno)
        print(address)
        user.objects.create(name=name, password=pas, email=email, ph=phoneno, add=address)
        return render(request, 'login.html')
    return render(request, 'registration.html')

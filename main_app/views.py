from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import StudentInfo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return render(request,"login.html")

def about(request):
    return render(request,"about.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html",{"messege":"Invalid Credentials."})
    else:   
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html", {"messege":"LOGGED OUT"})



@csrf_exempt
def add_student(request):

    if request.method == "POST":

        name = request.POST["name"]   
        id = request.POST["id"]
        department=request.POST["department"]
        section = request.POST["section"]
        payment=request.POST["payment"]

        if name=="" or id =="" or section=="":
            msg = "Please Enter Name,Id and Section"

        elif StudentInfo.objects.filter(id=id).exists():
            msg = "ID Already Exists!"
        else:
            student = StudentInfo(name=name,id=id,department=department,section=section,payment=payment)
            student.save()
            msg = "Student registered Sucessfully"

        return render(request, "add_reg.html", {"msg": msg})
    else:
        return render(request, "add_reg.html")
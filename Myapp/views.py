from django.shortcuts import render, redirect
from django.http import HttpResponse 
from Myapp.models import Person
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    all_person = Person.objects.all()
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    students = ['โฟ', 'โฟน', 'บาส', 'ไอซ์']
    return render(request,"about.html",{"studentskey":students})

def form (request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        person = Person.objects.create(
            name = name,
            age = age
            )
        person.save
        return redirect("/")
    else:
        return render(request,"form.html")

def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect("/")

def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

def JavaScript_Exercises(request):
    return render(request,"JavaScript_Exercises.html")
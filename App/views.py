from django.shortcuts import render, redirect
from App.models import Students

# Create your views here.

def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        user = Students.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone)
        user.save()
        return redirect('/read/')
    return render(request,'create.html')


def read(request):
    reads = Students.objects.all().order_by('id')
    return render(request,'read.html', {'reads':reads})


def edit(request,id):
    edits = Students.objects.get(id=id)
    return render(request,'edit.html',{'edits':edits})


def update(request,id):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        updates = Students.objects.get(id=id)
        updates.first_name=first_name
        updates.last_name=last_name
        updates.email=email
        updates.phone=phone
        updates.save()

        return redirect('read')
    return render(request,'edit.html')


def delete(request,id):
    dels = Students.objects.get(id=id)
    dels.delete()
    return redirect('read')






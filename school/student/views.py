from django.shortcuts import render,redirect
from .models import Student
from . forms import StudentForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=="POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfull!')
            return redirect('home')
    else:
        form = StudentForm()
    context = {
        'form':form
    }
    return render(request, 'index.html',context)



def read(request):
    records = Student.objects.all()
    context = {
        'records':records
    }
    return render(request, 'read.html',context)


def edit(request,id):
    record = Student.objects.get(id=id)
    form = StudentForm(instance=record)
    if request.method=="POST":
        form = StudentForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = StudentForm(instance=record)
    context = {
        'form':form
    }
    return render(request, 'edit.html',context)




def delete(request,id):
    record = Student.objects.get(id=id)
    record.delete()
    messages.success(request, 'Record Has been deleted! ')

    return redirect('read')
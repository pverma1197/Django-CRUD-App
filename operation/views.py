from django.shortcuts import render
from .models import User
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.
#Create and Read Records
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pas)
            reg.save()
            fm = StudentRegistration()
            return HttpResponseRedirect(request.path)
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'operation/addandshow.html', {'form':fm, 'stu':stud})

#Delete Record
def delete_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')
#Edit Record

def update_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'operation/update.html', {'form': fm})

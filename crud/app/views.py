from django.shortcuts import render,redirect
from app.models import Details
from app.forms import Detailsform
from django.http import HttpResponse
# Create your views here.
def views(request):
    obj= Details.objects.all()
    return render(request,'views.html',{'data':obj})


def create(request):
    if request.method=="POST":
        form=Detailsform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('create')
    else:
        form=Detailsform


    
    form=Detailsform()
    context={
        'form':form
    }
    
    
    return render(request,'create.html',context)

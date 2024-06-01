from django.http import HttpResponse
from django.shortcuts import  render
from app_crud.forms import EmployeeForm
from app_crud.models import Employee
from django.db.models import Q
# Create your views here.

def Index(request):
    if "q" in request.GET:
        q=request.GET['q']
        obj=Employee.objects.filter(Q(name__icontains=q )|Q(contact__icontains=q))
    else:
        obj=Employee.objects.all()
    return render(request,'edit.html',{'data':obj})

def Create(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Added successfully')
    else:
        form=EmployeeForm
    context={
        'form':form
    }
    return render(request,'create.html',context  )

def Delete(request,id):
    obj=Employee.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponse('Deleted Successfully')
    return render(request,'delete.html', {'object': obj})

def Update(request,id):
    obj=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated successfully')
    else:
        form=EmployeeForm
    context={
        'form':form
    }
    return render(request,'update.html',context)


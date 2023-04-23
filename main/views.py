from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import Company,Employee
from django.db.models import Q

# Create your views here.


def companies_view(request):
    context = {
        "companies": Company.objects.all(),
        "employees": Employee.objects.all(),
    }
    return render(request, 'companies.html',context )

def employees_view(request,id):
    if request.method == 'POST' and 'sub' in request.POST:
        query = request.POST.get('query')
        allEmployees = Employee.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        return render(request, 'employees.html', {"employees": allEmployees,"query":query})
    elif request.method == 'POST' and 'add' in request.POST:
        emp_name = request.POST.get('employee')
        emp_fname = emp_name.split()[0]
        emp_sname = emp_name.split()[1]
        emp = Employee.objects.filter(Q(first_name__icontains=emp_fname) & Q(last_name__icontains=emp_sname))
        comp = Company.objects.get(id=id)
        emp.update(companies = comp)
        return redirect('/')
    else:
        allEmployees = Employee.objects.all()
        return render(request, 'employees.html', {"employees": allEmployees})

from django.shortcuts import render

def home(request):
    employees = [
        {"name": "Rahul", "job": "Manager", "salary": 50000, "full_time": True},
        {"name": "Asha", "job": "Designer", "salary": 30000, "full_time": False},
        {"name": "Vikram", "job": "Developer", "salary": 45000, "full_time": True},
    ]

    return render(request, 'employee/index.html', {"employees": employees})

from django.shortcuts import render

def students_view(request):
    students = [
        {"name": "Rohan", "grade": "A", "passed": False},
        {"name": "Priya", "grade": "C", "passed": False},
        {"name": "Aryan", "grade": "B", "passed": True},
    ]

    return render(request, "classroom/students.html", {"students": students})

from django.shortcuts import render

def home(request):
    return render(request, 'main/form.html')

def result(request):
    name = request.POST.get('name')
    color = request.POST.get('color')

    return render(request, 'main/result.html', {
        'name': name,
        'color': color
    })

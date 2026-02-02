from django.shortcuts import render

def home(request):
    return render(request, 'main/form.html')

def result(request):
    username = request.GET.get('username')
    return render(request, 'main/result.html', {
        'username': username
    })

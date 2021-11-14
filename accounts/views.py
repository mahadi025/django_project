from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User name already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(
                    request, 'This email is already register with an account')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                messages.info(request, 'User Created')
                return redirect('index')
        else:
            messages.info(request, 'Password did not match')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard.html')  # 👈 Redirects to dashboard.html
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


# users/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User
from .decorators import role_required

@login_required
@role_required('admin', 'gdg', 'hod')
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


# users/views.py
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

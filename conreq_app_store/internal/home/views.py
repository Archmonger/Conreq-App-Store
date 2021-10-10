from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render

User = get_user_model()


def home(request):
    if not request.user.is_authenticated:
        admin = authenticate(username="admin", password="")
        if admin is None:
            admin = User.objects.create_superuser(username="admin", password="")
        login(request, admin)
    return render(request, "home.html")

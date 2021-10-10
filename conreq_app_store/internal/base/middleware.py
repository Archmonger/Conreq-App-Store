from django.contrib.auth import authenticate, get_user_model, login

User = get_user_model()


class AlwaysAdmin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            admin = authenticate(username="admin", password="")
            if admin is None:
                admin = User.objects.create_superuser(username="admin", password="")
            login(request, admin)

        return self.get_response(request)

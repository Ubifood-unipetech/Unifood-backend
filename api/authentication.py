from django.contrib.auth import login, authenticate, logout
from rest_framework_simplejwt.views import TokenObtainPairView

class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user:
            login(request, user)
        return response
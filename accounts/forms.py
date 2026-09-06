from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User # どの Model のユーザーを作成するか
        fields = ("username", "email")

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class Register(UserCreationForm):
    pass


class Login(AuthenticationForm):
    pass

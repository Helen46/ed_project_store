from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StileFormMixin
from users.models import User


class UserRegisterForm(StileFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phon", "avatar")

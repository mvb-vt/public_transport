from django.contrib.auth import forms as auth_forms

from public_transport.accounts.models import UserProfiles


class BusUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserProfiles
        fields = ('username', 'email')

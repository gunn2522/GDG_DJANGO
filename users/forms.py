from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'erp_number', 'email', 'role')  # Add other custom fields as needed

    def clean_erp_number(self):
        erp = self.cleaned_data['erp_number']
        if User.objects.filter(erp_number=erp).exists():
            raise forms.ValidationError("A user with this ERP number already exists.")
        return erp

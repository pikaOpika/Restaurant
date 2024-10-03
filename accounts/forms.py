from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CookCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('years_of_experience', 'description', 'image')

        description = forms.CharField(
            widget=forms.Textarea(attrs={'rows': 3}),
            required=False
        )
        image = forms.ImageField(required=False)

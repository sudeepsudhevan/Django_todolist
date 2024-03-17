from django import forms
from .models import Todo


class todoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "myinput", "placeholder": "Enter your todo..."}
        )
    )

    class Meta:
        model = Todo
        fields = ["title"]

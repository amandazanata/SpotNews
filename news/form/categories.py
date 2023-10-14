from django import forms

from news.models import Categories


class Categories_forms(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

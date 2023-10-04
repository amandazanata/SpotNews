from django import forms

from news.models.news_model import News


class News_form(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            "categories": forms.CheckboxSelectMultiple(),
            "created_at": forms.DateInput(attrs={"type": "date"}),
        }

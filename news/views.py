from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from news.forms import CategoriesForm

# Create your views here.


def home(request):
    new = {"news_list": News.objects.all()}
    return render(request, "home.html", new)


def details_page(request, id):
    new = {"news": get_object_or_404(News, id=id)}
    return render(request, "news_details.html", new)


# Req 6
def forms_categories(request):
    form = CategoriesForm()
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect("home-page")

    return render(request, "categories_form.html", {"form": form})

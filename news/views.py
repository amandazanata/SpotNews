from django.shortcuts import redirect, render

from news.form.categories import Categories_forms  # type: ignore
from news.form.news import News_form  # type: ignore
from news.models import News  # type: ignore


def home_view(request):
    news = News.objects.all()  # type: ignore
    return render(request, "home.html", {"news": news})


def details_view(request, id):
    news = News.objects.get(id=id)  # type: ignore
    return render(request, "news_details.html", {"details": news})


def categories_view(request):
    form = (
        Categories_forms(request.POST)
        if request.method == "POST"
        else Categories_forms()
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home-page")

    return render(request, "categories_form.html", {"form": form})


def news_view(request):
    form = (
        News_form(request.POST, request.FILES)
        if request.method == "POST"
        else News_form()
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home-page")

    return render(request, "news_form.html", {"form": form})

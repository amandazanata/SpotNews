from django.urls import path
from news.views import home, details_page, forms_categories  # views.py

# from . import views

urlpatterns = [
    path("", home, name="home-page"),
    path("news/", home, name="news-details-page"),
    path("<int:id>", details_page, name="news-details-page"),
    path("categories", forms_categories, name="categories-form"),
]

from django.urls import path

from news.views import categories_view, details_view, home_view, news_view

urlpatterns = [
    path("", home_view, name="home-page"),
    path("news/<int:id>", details_view, name="news-details-page"),
    path("categories", categories_view, name="categories-form"),
    path("news", news_view, name="news-form"),
]

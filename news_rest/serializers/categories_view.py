from rest_framework import viewsets

from news.models import Categories
from news_rest.serializers.categories_serializer import (
    CategoriesSerializer as _,
)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = _

from rest_framework import viewsets

from news.models import Categories  # type: ignore
from news_rest.serializers.categories_serializer import (  # type: ignore
    CategoriesSerializer as _,
)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()  # type: ignore
    serializer_class = _

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from news.models.category_model import Categories
from news.models.user_model import Users


class News(models.Model):
    def not_single_word(value):  # type: ignore
        # MIN_SIZE = 1
        if len(value.split()) <= 1:  # type: ignore
            raise ValidationError(
                "O título deve conter pelo menos 2 palavras.",
                # params={"size": MIN_SIZE},
            )

    title = models.CharField(
        validators=[
            not_single_word,
        ],
        max_length=200,
    )
    content = models.TextField(
        validators=[
            MinLengthValidator(1, "Este campo não pode estar vazio."),
        ],
    )
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="img/",
        blank=True,
    )

    categories = models.ManyToManyField(Categories, related_name="news")
    created_at = models.DateField()

    def __str__(self):
        return self.title

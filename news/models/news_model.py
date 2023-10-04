from django.db import models
from .validators import validate_title


# Req 3
class News(models.Model):
    title = models.CharField(
        max_length=200, blank=False, null=False, validators=[validate_title]
    )

    content = models.TextField()

    author = models.ForeignKey("Users", on_delete=models.CASCADE)

    created_at = models.DateField(blank=False, null=False)

    image = models.ImageField(upload_to="img/", blank=True, null=True)

    categories = models.ManyToManyField("Categories", blank=True, null=True)

    def __str__(self):
        return self.title

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import news.models.news_model


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("role", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[
                            news.models.news_model.News.not_single_word
                        ],
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        validators=[
                            django.core.validators.MinLengthValidator(
                                1, "Este campo não pode estar vazio."
                            )
                        ]
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="img/")),
                ("created_at", models.DateField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.users",
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="news", to="news.categories"
                    ),
                ),
            ],
        ),
    ]

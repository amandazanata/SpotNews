from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="categories",
            field=models.ManyToManyField(
                blank=True, null=True, to="news.categories"
            ),
        ),
    ]

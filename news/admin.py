from django.contrib import admin
from .models import Categories, News, Users

# Register your models here.

admin.site.register(Categories)
admin.site.register(News)
admin.site.register(Users)

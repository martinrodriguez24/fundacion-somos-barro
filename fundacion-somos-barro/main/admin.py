from django.contrib import admin
from .models import User, News, Comment

admin.site.register(User)
admin.site.register(News)
admin.site.register(Comment)



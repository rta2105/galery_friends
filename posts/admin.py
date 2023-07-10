from django.contrib import admin
from .models import Posts

admin.site.register(Posts, admin.ModelAdmin)

# Register your models here.

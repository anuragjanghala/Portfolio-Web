from django.contrib import admin

# Register your models here.

from .models import Project, Tag, Message

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Message)
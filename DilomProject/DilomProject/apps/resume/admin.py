from django.contrib import admin

from .models import Resume, Comment , Images, Position_Area
# Register your models here.

admin.site.register(Resume)
admin.site.register(Comment)
admin.site.register(Images)
admin.site.register(Position_Area)
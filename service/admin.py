from django.contrib import admin

from service import models

# Register your models here.
admin.site.register(models.Login),
admin.site.register(models.Feedback),
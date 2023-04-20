from django.contrib import admin

from service import models

# Register your models here.
admin.site.register(models.Login),
admin.site.register(models.Feedback),
admin.site.register(models.Appointment),
admin.site.register(models.Schedule),
admin.site.register(models.WorkerCategory),
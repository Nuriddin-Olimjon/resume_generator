from django.contrib import admin
from main import models


admin.site.register(models.User)
admin.site.register(models.Region)
admin.site.register(models.Link)
admin.site.register(models.Language)
admin.site.register(models.EducationEmployment)

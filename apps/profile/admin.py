from django.contrib import admin
from apps.profile import models


admin.site.register(models.User)
admin.site.register(models.Region)
admin.site.register(models.Link)
admin.site.register(models.Language)
admin.site.register(models.EducationEmployment)

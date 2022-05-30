from django.contrib import admin
from .models import Command, CommandType, CommandTypeText

# Register your models here.
admin.site.register(Command)
admin.site.register(CommandType)
admin.site.register(CommandTypeText)

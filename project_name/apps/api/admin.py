from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import UploadFile

TokenAdmin.raw_id_fields = ('user',)


class UploadFileAdmin(admin.ModelAdmin):
    model = UploadFile

admin.site.register(UploadFile, UploadFileAdmin)

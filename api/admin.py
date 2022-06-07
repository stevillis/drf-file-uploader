from django.contrib import admin

from api.models import DocumentVersion


@admin.register(DocumentVersion)
class DocumentVersionAdmin(admin.ModelAdmin):
    fields = ['name', 'doc_file', ]
    list_display = ['name', 'doc_file', ]

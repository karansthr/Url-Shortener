from django.contrib import admin
from . import models


class DocAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Doc

    list_display = ["title", "timestamp"]
    list_display_links = ["timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]


admin.site.register(models.Doc, DocAdmin)

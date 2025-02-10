from django.contrib import admin
from apps.same.models import ArquivamentoSame
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ArquivamentoResouce(resources.ModelResource):
    class Meta:
        model = ArquivamentoSame


class ArquivamentoAdmin(ImportExportModelAdmin):
    resource_class = ArquivamentoResouce


admin.site.register(ArquivamentoSame, ArquivamentoAdmin)

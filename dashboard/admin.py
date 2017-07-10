from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from django.contrib import admin
from dashboard.models import Outpatient

# Register your models here.

class OutpatientResource(ModelResource):

    class Meta:
        model = Outpatient

class OutpatientAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = OutpatientResource
    list_display = ('last_name', 'first_name', 'age', 'address', 'doctors_note', 'medication_1', 'medication_2', 'medication_3', 'medication_4', 'visit_date', 'reminder_schedule_1_date', 'reminder_frequency')

admin.site.register(Outpatient, OutpatientAdmin)

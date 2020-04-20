from django.contrib import admin
from .models import Scheme, ComputationData, IdentificationNumber, Project, SSN, MasterList


class SchemeAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('scheme_id', 'description', 'date_created', 'owner', 'revision', 'archived')
    list_filter = ['date_created', 'owner', 'revision']
    search_fields = ['scheme_id', 'description']

class ComputationDataAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('comp_data_id', 'description', 'date_created', 'owner', 'revision', 'archived')
    list_filter = ['date_created', 'owner', 'revision']
    search_fields = ['comp_data_id', 'description']

class IdentificationNumberAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('id_number_id', 'description', 'date_created', 'owner', 'revision', 'archived')
    list_filter = ['date_created', 'owner', 'revision']
    search_fields = ['id_number_id', 'description']

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('project_id', 'description', 'date_created', 'owner', 'revision', 'archived')
    list_filter = ['date_created', 'owner', 'revision', 'archived']
    search_fields = ['project_id', 'description']

class SSNAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('ssn_id', 'description', 'date_created', 'owner', 'revision', 'archived')
    list_filter = ['date_created', 'owner', 'revision', 'archived']
    search_fields = ['ssn_id', 'description']

class MasterListAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('master_list_id', 'description', 'date_created', 'owner', 'revision', 'archived')
    list_filter = ['date_created', 'owner', 'revision', 'archived']
    search_fields = ['master_list_id', 'description']


admin.site.register(Scheme, SchemeAdmin)
admin.site.register(ComputationData, ComputationDataAdmin)
admin.site.register(IdentificationNumber, IdentificationNumberAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(SSN, SSNAdmin)
admin.site.register(MasterList, MasterListAdmin)
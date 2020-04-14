from django.contrib import admin
from .models import Scheme, ComputationData, IdentificationNumber


class SchemeAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('scheme_id', 'description', 'date_created', 'owner')
    list_filter = ['date_created', 'owner']
    search_fields = ['scheme_id', 'description']

class ComputationDataAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('comp_data_id', 'description', 'date_created', 'owner')
    list_filter = ['date_created', 'owner']
    search_fields = ['comp_data_id', 'description']

class IdentificationNumberAdmin(admin.ModelAdmin):
    fieldsets = None
    list_display = ('id_number_id', 'description', 'date_created', 'owner')
    list_filter = ['date_created', 'owner']
    search_fields = ['id_number_id', 'description']


admin.site.register(Scheme, SchemeAdmin)
admin.site.register(ComputationData, ComputationDataAdmin)
admin.site.register(IdentificationNumber, IdentificationNumberAdmin)
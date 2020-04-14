from django.db import models
from django.conf import settings

def increment_scheme_number():
    last_scheme = Scheme.objects.all().order_by('id').last()
    if not last_scheme:
        return 'D' + '102000'
    scheme_id = last_scheme.scheme_id
    scheme_int = int(scheme_id[1:7])
    new_scheme_int = scheme_int + 1
    new_scheme_id = 'D' + str(new_scheme_int).zfill(6)
    return new_scheme_id

# nacrti - D
class Scheme(models.Model):
    scheme_id = models.CharField(max_length=7, default=increment_scheme_number, editable=False)
    description = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='schemes', on_delete=models.CASCADE)

    def __str__(self):
        return self.scheme_id



def increment_computation_data_number():
    last_comp_data = ComputationData.objects.all().order_by('id').last()
    if not last_comp_data:
        return 'CD' + '1100'
    comp_data_id = last_comp_data.comp_data_id
    comp_data_int = int(comp_data_id[2:6])
    new_comp_data_int = comp_data_int + 1
    new_comp_data_id = 'CD' + str(new_comp_data_int).zfill(4)
    return new_comp_data_id

# proracunski podaci - CD
class ComputationData(models.Model):
    comp_data_id = models.CharField(max_length=6, default=increment_computation_data_number, editable=False)
    description = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='computation_data', on_delete=models.CASCADE)

    def __str__(self):
        return self.description



def increment_id_number():
    last_id_number = IdentificationNumber.objects.all().order_by('id').last()
    if not last_id_number:
        return 'ID' + '100001'
    id_number_id = last_id_number.id_number_id
    id_number_int = int(id_number_id[2:8])
    new_id_number_int = id_number_int + 1
    new_id_number_id = 'ID' + str(new_id_number_int).zfill(6)
    return new_id_number_id

# proracunski podaci - CD
class IdentificationNumber(models.Model):
    id_number_id = models.CharField(max_length=8, default=increment_id_number, editable=False)
    description = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='id_numbers', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

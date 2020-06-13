from django.db import models
from django.conf import settings
from django.db import transaction

class RevisionChoices(models.TextChoices):
    A = 'A',
    B = 'B',
    C = 'C',
    D = 'D',
    E = 'E',
    F = 'F',
    G = 'G',
    H = 'H',
    I = 'I',
    J = 'J',
    K = 'K',
    L = 'L',
    M = 'M',
    N = 'N'


def increment_scheme_number():
    last_scheme = Scheme.objects.select_for_update().all().order_by('id').last()
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
    revision = models.CharField(max_length=1, choices=RevisionChoices.choices, blank=True, default=None, null=True)
    archived = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='schemes', on_delete=models.CASCADE)

    def __str__(self):
        return self.scheme_id



def increment_computation_data_number():
    last_comp_data = ComputationData.objects.select_for_update().all().order_by('id').last()
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
    revision = models.CharField(max_length=1, choices=RevisionChoices.choices, blank=True, default=None, null=True)
    archived = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='computation_data', on_delete=models.CASCADE)

    def __str__(self):
        return self.description



def increment_id_number():
    last_id_number = IdentificationNumber.select_for_update().objects.all().order_by('id').last()
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
    revision = models.CharField(max_length=1, choices=RevisionChoices.choices, blank=True, default=None, null=True)
    archived = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='id_numbers', on_delete=models.CASCADE)

    def __str__(self):
        return self.description



def increment_ssn_number():
    last_ssn = SSN.objects.select_for_update().all().order_by('id').last()
    if not last_ssn:
        return 'SSN' + '1001'
    ssn_id = last_ssn.ssn_id
    ssn_int = int(ssn_id[3:7])
    new_ssn_int = ssn_int + 1
    new_ssn_id = 'SSN' + str(new_ssn_int).zfill(4)
    return new_ssn_id

# shema spajanja namota - SSN
class SSN(models.Model):
    ssn_id = models.CharField(max_length=7, default=increment_ssn_number, editable=False)
    description = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    revision = models.CharField(max_length=1, choices=RevisionChoices.choices, blank=True, default=None, null=True)
    archived = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ssn', on_delete=models.CASCADE)

    def __str__(self):
        return self.description



def increment_project_number():
    last_project = Project.objects.select_for_update().all().order_by('id').last()
    if not last_project:
        return 'PR' + '3100'
    project_id = last_project.project_id
    project_int = int(project_id[2:6])
    new_project_int = project_int + 1
    new_project_id = 'PR' + str(new_project_int).zfill(4)
    return new_project_id

# projekt - PR
class Project(models.Model):
    project_id = models.CharField(max_length=6, default=increment_project_number, editable=False)
    description = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    revision = models.CharField(max_length=1, choices=RevisionChoices.choices, blank=True, default=None, null=True)
    archived = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.description



def increment_master_list_number():
    last_master_list = MasterList.select_for_update().objects.all().order_by('id').last()
    if not last_master_list:
        return 'ML' + '1001'
    master_list_id = last_master_list.master_list_id
    master_list_int = int(master_list_id[2:6])
    new_master_list_int = master_list_int + 1
    new_master_list_id = 'ML' + str(new_master_list_int).zfill(4)
    return new_master_list_id

# projekt - PR
class MasterList(models.Model):
    master_list_id = models.CharField(max_length=6, default=increment_master_list_number, editable=False)
    description = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    revision = models.CharField(max_length=1, choices=RevisionChoices.choices, blank=True, default=None, null=True)
    archived = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='masterlists', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

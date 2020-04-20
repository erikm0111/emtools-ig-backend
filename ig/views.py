from rest_framework import viewsets

from .serializers import SchemeSerializer, ComputationDataSerializer, IdentificationNumberSerializer, ProjectSerializer, MasterListSerializer, SSNSerializer
from .models import Scheme, ComputationData, IdentificationNumber, Project, SSN, MasterList

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Scheme.objects.order_by('-id')


class ComputationDataViewSet(viewsets.ModelViewSet):
    queryset = ComputationData.objects.all()
    serializer_class = ComputationDataSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return ComputationData.objects.order_by('-id')


class IdentificationNumberViewSet(viewsets.ModelViewSet):
    queryset = IdentificationNumber.objects.all()
    serializer_class = IdentificationNumberSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return IdentificationNumber.objects.order_by('-id')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Project.objects.order_by('-id')


class SSNViewSet(viewsets.ModelViewSet):
    queryset = SSN.objects.all()
    serializer_class = SSNSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return SSN.objects.order_by('-id')


class MasterListViewSet(viewsets.ModelViewSet):
    queryset = MasterList.objects.all()
    serializer_class = MasterListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return MasterList.objects.order_by('-id')


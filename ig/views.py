from rest_framework import viewsets
from django.db import transaction

from .serializers import SchemeSerializer, ComputationDataSerializer, IdentificationNumberSerializer, ProjectSerializer, MasterListSerializer, SSNSerializer, QInquirySerializer
from .models import Scheme, ComputationData, IdentificationNumber, Project, SSN, MasterList, QInquiry


class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Scheme.objects.order_by('-id')


class ComputationDataViewSet(viewsets.ModelViewSet):
    queryset = ComputationData.objects.all()
    serializer_class = ComputationDataSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return ComputationData.objects.order_by('-id')


class IdentificationNumberViewSet(viewsets.ModelViewSet):
    queryset = IdentificationNumber.objects.all()
    serializer_class = IdentificationNumberSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return IdentificationNumber.objects.order_by('-id')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Project.objects.order_by('-id')


class SSNViewSet(viewsets.ModelViewSet):
    queryset = SSN.objects.all()
    serializer_class = SSNSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return SSN.objects.order_by('-id')


class MasterListViewSet(viewsets.ModelViewSet):
    queryset = MasterList.objects.all()
    serializer_class = MasterListSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return MasterList.objects.order_by('-id')


class QInquiryViewSet(viewsets.ModelViewSet):
    queryset = QInquiry.objects.all()
    serializer_class = QInquirySerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @transaction.atomic
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return QInquiry.objects.order_by('-id')


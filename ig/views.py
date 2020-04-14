from rest_framework import viewsets

from .serializers import SchemeSerializer, ComputationDataSerializer, IdentificationNumberSerializer
from .models import Scheme, ComputationData, IdentificationNumber

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return reversed(Scheme.objects.all())


class ComputationDataViewSet(viewsets.ModelViewSet):
    queryset = ComputationData.objects.all()
    serializer_class = ComputationDataSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return reversed(ComputationData.objects.all())


class IdentificationNumberViewSet(viewsets.ModelViewSet):
    queryset = IdentificationNumber.objects.all()
    serializer_class = IdentificationNumberSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return reversed(IdentificationNumber.objects.all())

from rest_framework import serializers
from .models import Scheme, ComputationData, IdentificationNumber

class SchemeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Scheme
        fields = ('id', 'scheme_id', 'description', 'date_created', 'owner')
        read_only_fields = ('id', 'scheme_id', 'date_created', 'owner')


class ComputationDataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ComputationData
        fields = ('id', 'comp_data_id', 'description', 'date_created', 'owner')
        read_only_fields = ('id', 'comp_data_id', 'date_created', 'owner')


class IdentificationNumberSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = IdentificationNumber
        fields = ('id', 'id_number_id', 'description', 'date_created', 'owner')
        read_only_fields = ('id', 'id_number_id', 'date_created', 'owner')

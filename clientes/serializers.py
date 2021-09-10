from rest_framework import serializers
from clientes.models import Cliente
import re

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("Cpf deve conter 11 digitos")
        return cpf

    
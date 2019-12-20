from rest_framework import serializers
from .models import TipoLancamento, Lancamento, Receita


class TipoLancamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLancamento
        fields = '__all__'


class LancamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lancamento
        fields = '__all__'


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
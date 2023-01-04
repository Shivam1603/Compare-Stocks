from rest_framework import serializers
from .models import Security

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ['id', 'name', 'prev_close', 'pe_ratio', 'dividend_yield', 'primary_exchange']
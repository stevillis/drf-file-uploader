from .models import DocumentVersion

from rest_framework import serializers


class DocumentVersionSerializer(serializers.ModelSerializer):
    """DocumentVersion Serializer"""
    class Meta:
        """Medata options"""
        model = DocumentVersion
        fields = '__all__'

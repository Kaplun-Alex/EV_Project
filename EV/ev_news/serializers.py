from rest_framework import serializers
from .models import Headline


class HeadlineSerializer(serializers.Serializer):
    class Meta:
        model = Headline
        fields = '__all__'

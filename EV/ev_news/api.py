from .models import Headline
from rest_framework import viewsets, permissions
from .serializers import HeadlineSerializer


class HeadlineViewSet(viewsets.ModelViewSet):
    queryset = Headline.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HeadlineSerializer

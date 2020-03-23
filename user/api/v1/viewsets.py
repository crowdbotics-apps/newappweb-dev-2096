from rest_framework import authentication
from user.models import HHGH
from .serializers import HHGHSerializer
from rest_framework import viewsets


class HHGHViewSet(viewsets.ModelViewSet):
    serializer_class = HHGHSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HHGH.objects.all()

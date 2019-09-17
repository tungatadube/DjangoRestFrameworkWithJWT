from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = (IsAuthenticated,)



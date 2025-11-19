from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import ActorSerialize
from app.permissions import GlobalDefaultPermission


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerialize


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerialize

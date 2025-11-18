from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import ActorSerialize


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerialize


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerialize

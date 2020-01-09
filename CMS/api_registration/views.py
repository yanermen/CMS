from django.contrib.auth.models import User
from django.contrib.auth import admin

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response


from .models import PersonData
from .serializers import PersonDataSerializer, UserSerializer, AdminSerializer
from .permissions import IsOwnerOrReadOnly


class PersonDataList(generics.ListCreateAPIView):
    queryset = PersonData.objects.all()
    serializer_class = PersonDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PersonDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonData.objects.all()
    serializer_class = PersonDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PersonDataHighlight(generics.GenericAPIView):
    queryset = PersonData.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'api_registration': reverse('PersonDataList', request=request, format=format)
    })


def get(self, request, *args, **kwargs):
    cms = self.get_object()
    return Response(cms.highlighted)


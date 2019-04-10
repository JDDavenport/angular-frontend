from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.serializers import UserSerializer, GroupSerializer, PrescriberSerializer, OverdosesSerializer, DocDrugQtySerializer, DangerScoreSerializer
from tutorial.models import prescriber, overdoses, docdrugqty, dangerscore

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PrescriberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = prescriber.objects.all()
    serializer_class = PrescriberSerializer

class OverdosesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = overdoses.objects.all()
    serializer_class = OverdosesSerializer

class DocDrugQtyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = docdrugqty.objects.all()
    serializer_class = DocDrugQtySerializer

class DangerScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = dangerscore.objects.all()
    serializer_class = DangerScoreSerializer

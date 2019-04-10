from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.models import prescriber, overdoses, docdrugqty, dangerscore

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PrescriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = prescriber
        fields = ('DoctorID', 'fname', 'lname', 'gender', 'state', 'credentials', 'specialty', 'OpioidPrescriber', 'totalprescriptions')

class OverdosesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = overdoses
        fields = ('state', 'population', 'deaths', 'abbrev')

class DocDrugQtySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = docdrugqty
        fields = ('DoctorID', 'drug', 'qty')

class DangerScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dangerscore
        fields = ('DoctorID', 'dangerscore')


from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models import Contact, ContactType
from api.permissions import IsObjMember


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=ContactType.objects.all())
    type_info = ContactTypeSerializer(source='type', read_only=True)
    
    class Meta:
        model = Contact
        fields = '__all__'
        extra_fields = ['type_mnemo', 'type_id']

class ContactTypes(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Contact types.
    """
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer
    permission_classes = [IsAdminUser]

class Contacts(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Contacts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsObjMember]
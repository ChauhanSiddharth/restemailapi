from .models import EmailModel
from rest_framework import serializers

class EmailSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailModel
        fields = ('sender_email', 'receiver_email','receiver_name','subject','message','message_delete','message_archive','message_sent','id')

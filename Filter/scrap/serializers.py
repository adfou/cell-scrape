from rest_framework import serializers
from .models import Head,fichie
class HeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Head 
        fields = ('pk', 't_ype', 'father', 'text', 'paragraph')

class fichieSerializer(serializers.ModelSerializer):

    class Meta:
        model = fichie 
        fields = ('pk', 'text_f', 'father')
       
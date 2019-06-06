from rest_framework import serializers

from .models import Talk


class TalkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talk
        fields = ('id', 'name', 'speaker', 'venue', 'talk_start', 'talk_end')

    def GetTalks(self):
        return
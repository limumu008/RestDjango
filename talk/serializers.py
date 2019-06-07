from rest_framework import serializers

from .models import Talk


class TalkSerializer(serializers.ModelSerializer):
    talk_start = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    talk_end = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    class Meta:
        model = Talk
        fields = ('id', 'name', 'speaker', 'venue', 'talk_start', 'talk_end')
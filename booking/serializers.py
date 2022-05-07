from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import ConferenceBooking


class ConferenceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceBooking
        fields = '__all__'

    def create(self, validated_data):
        data = ConferenceBooking.objects.filter(**validated_data)
        print(data)
        #
        if data.exists():
            raise ValidationError("It is busy at that time")
        conference_booking = ConferenceBooking.objects.create(**validated_data)
        return conference_booking

from rest_framework import serializers

from .models import Conference, Image


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ConferenceSerializer, self).to_representation(instance)
        if instance.image_set.exists():
            representation['images'] = ImageSerializer(instance.image_set.all(),
                                                         many=True).data
        else:
            representation['images'] = []
        return representation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

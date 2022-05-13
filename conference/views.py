from rest_framework import generics

from conference.models import Conference
from conference.paginators import ConferencePagination
from conference.serializers import ConferenceSerializer


class ConferenceListAPIView(generics.ListAPIView):
    serializer_class = ConferenceSerializer
    queryset = Conference.objects.all()
    pagination_class = ConferencePagination

    # have to write all parameters of filter, otherwise it will ignore
    def get_queryset(self):
        queryset = Conference.objects.all()
        conference_type = self.request.query_params.get('conference_type')
        projector = self.request.query_params.get('projector')
        conditioner = self.request.query_params.get('conditioner')
        board = self.request.query_params.get('board')
        if conference_type:
            queryset = queryset.filter(
                conference_type__icontains=conference_type, projector__icontains=projector,
                conditioner__icontains=conditioner, board__icontains=board,
            )
        return queryset


class ConferenceDetailAPIView(generics.RetrieveAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

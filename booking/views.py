from rest_framework import generics
from rest_framework.generics import get_object_or_404

from booking.models import ConferenceBooking
from booking.paginators import BookingPagination
from booking.serializers import ConferenceBookingSerializer


class ConferenceBookingListAPIView(generics.ListAPIView):
    serializer_class = ConferenceBookingSerializer
    queryset = ConferenceBooking.objects.all()
    pagination_class = BookingPagination

    def get_queryset(self):
        queryset = ConferenceBooking.objects.all()
        conference = self.request.query_params.get('conference')
        if conference:
            queryset = queryset.filter(
                conference=conference,
            )
        return queryset


class ConferenceBookingCreateAPIView(generics.CreateAPIView):
    queryset = ConferenceBooking.objects.all()
    serializer_class = ConferenceBookingSerializer


class ConferenceBookingDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConferenceBookingSerializer
    queryset = ConferenceBooking.objects.all()


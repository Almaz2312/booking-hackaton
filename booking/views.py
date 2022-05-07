from rest_framework import generics

from booking.models import ConferenceBooking
from booking.paginators import BookingPagination
from booking.serializers import ConferenceBookingSerializer


class ConferenceBookingListAPIView(generics.ListAPIView):
    serializer_class = ConferenceBookingSerializer
    queryset = ConferenceBooking.objects.all()
    pagination_class = BookingPagination


class ConferenceBookingCreateAPIView(generics.CreateAPIView):
    queryset = ConferenceBooking
    serializer_class = ConferenceBookingSerializer


class ConferenceBookingDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConferenceBookingSerializer
    queryset = ConferenceBooking



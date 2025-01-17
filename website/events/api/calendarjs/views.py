from django.db.models import Count, Prefetch, Q

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from events.api.calendarjs.permissions import UnpublishedEventPermissions
from events.api.calendarjs.serializers import (
    EventsCalenderJSSerializer,
    ExternalEventCalendarJSSerializer,
    UnpublishedEventsCalenderJSSerializer,
)
from events.api.v2 import filters
from events.models import Event, EventRegistration
from events.models.external_event import ExternalEvent
from utils.snippets import extract_date_range


class CalendarJSEventListView(ListAPIView):
    """Define a custom route that outputs the correctly formatted events information for CalendarJS, published events only."""

    serializer_class = EventsCalenderJSSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    filter_backends = (
        filters.EventDateFilter,
        filters.CategoryFilter,
        filters.OrganiserFilter,
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["member"] = self.request.member
        return context

    def get_queryset(self):
        start, end = extract_date_range(self.request)
        events = Event.objects.filter(
            end__gte=start, start__lte=end, published=True
        ).annotate(
            number_regs=Count(
                "eventregistration", filter=Q(eventregistration__date_cancelled=None)
            )
        )
        if self.request.member:
            events = events.prefetch_related(
                Prefetch(
                    "eventregistration_set",
                    to_attr="member_registration",
                    queryset=EventRegistration.objects.filter(
                        member=self.request.member
                    ).select_properties("queue_position"),
                )
            ).select_properties("participant_count")
        return events


class CalendarJSUnpublishedEventListView(ListAPIView):
    """Define a custom route that outputs the correctly formatted external events information for CalendarJS, unpublished events only."""

    queryset = Event.objects.filter(published=False)
    serializer_class = UnpublishedEventsCalenderJSSerializer
    permission_classes = [IsAdminUser, UnpublishedEventPermissions]
    pagination_class = None
    filter_backends = (
        filters.EventDateFilter,
        filters.CategoryFilter,
        filters.OrganiserFilter,
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["member"] = self.request.member
        return context


class CalendarJSExternalEventListView(ListAPIView):
    """Define a custom route that outputs the correctly formatted events information for CalendarJS, published events only."""

    queryset = ExternalEvent.objects.filter(published=True)
    serializer_class = ExternalEventCalendarJSSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    filter_backends = (
        filters.EventDateFilter,
        filters.CategoryFilter,
        filters.OrganiserFilter,
    )

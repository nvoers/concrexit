import mimetypes
from base64 import b64encode

from django.contrib.staticfiles.finders import find as find_static_file
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from rest_framework import serializers

from events.models import Event, Registration


class CalenderJSSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'start', 'end', 'all_day', 'is_birthday',
            'url', 'title', 'description',
            'backgroundColor', 'textColor', 'blank',
            'registered'
        )

    start = serializers.SerializerMethodField('_start')
    end = serializers.SerializerMethodField('_end')
    all_day = serializers.SerializerMethodField('_all_day')
    is_birthday = serializers.SerializerMethodField('_is_birthday')
    url = serializers.SerializerMethodField('_url')
    title = serializers.SerializerMethodField('_title')
    description = serializers.SerializerMethodField('_description')
    backgroundColor = serializers.SerializerMethodField('_background_color')
    textColor = serializers.SerializerMethodField('_text_color')
    blank = serializers.SerializerMethodField('_target_blank')
    registered = serializers.SerializerMethodField('_registered')

    def _start(self, instance):
        return timezone.localtime(instance.start)

    def _end(self, instance):
        return timezone.localtime(instance.end)

    def _all_day(self, instance):
        return False

    def _is_birthday(self, instance):
        return False

    def _url(self, instance):
        raise NotImplementedError

    def _title(self, instance):
        return instance.title

    def _description(self, instance):
        return strip_tags(instance.description)

    def _background_color(self, instance):
        pass

    def _text_color(self, instance):
        pass

    def _target_blank(self, instance):
        return False

    def _registered(self, instance):
        return None


class EventCalenderJSSerializer(CalenderJSSerializer):
    class Meta(CalenderJSSerializer.Meta):
        model = Event

    def _url(self, instance):
        return reverse('events:event', kwargs={'event_id': instance.id})

    def _registered(self, instance):
        try:
            return instance.is_member_registered(self.context['user'].member)
        except AttributeError:
            return None


class UnpublishedEventSerializer(CalenderJSSerializer):
    class Meta(CalenderJSSerializer.Meta):
        model = Event

    def _background_color(self, instance):
        return "#888888"

    def _text_color(self, instance):
        return "white"

    def _url(self, instance):
        return reverse('events:admin-details', kwargs={
            'event_id': instance.id})


class EventRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('pk', 'title', 'description', 'start', 'end', 'organiser',
                  'category', 'registration_start', 'registration_end',
                  'cancel_deadline', 'location', 'map_location', 'price',
                  'fine', 'max_participants', 'num_participants', 'status',
                  'user_registration', 'registration_allowed',
                  'no_registration_message', 'has_fields')

    description = serializers.SerializerMethodField('_description')
    user_registration = serializers.SerializerMethodField('_user_registration')
    num_participants = serializers.SerializerMethodField('_num_participants')
    registration_allowed = serializers.SerializerMethodField(
        '_registration_allowed')
    has_fields = serializers.SerializerMethodField('_has_fields')

    def _description(self, instance):
        return strip_tags(instance.description)

    def _num_participants(self, instance):
        return instance.num_participants()

    def _user_registration(self, instance):
        try:
            reg = instance.registration_set.get(
                member=self.context['request'].user.member)
            return {
                'registered_on': reg.date,
                'queue_position': reg.queue_position()
                if reg.queue_position() > 0 else None,
                'is_cancelled': reg.date_cancelled is not None,
                'is_late_cancellation': reg.is_late_cancellation(),
            }
        except Registration.DoesNotExist:
            return None

    def _registration_allowed(self, instance):
        member = self.context['request'].user.member
        return (member is not None and
                member.current_membership is not None and
                member.can_attend_events)

    def _has_fields(self, instance):
        return instance.has_fields()


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('pk', 'title', 'description', 'start', 'end',
                  'location', 'price', 'registered')

    description = serializers.SerializerMethodField('_description')
    registered = serializers.SerializerMethodField('_registered')

    def _description(self, instance):
        return strip_tags(instance.description)

    def _registered(self, instance):
        try:
            return instance.is_member_registered(
                self.context['request'].user.member)
        except AttributeError:
            return None


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('pk', 'member', 'name', 'photo')

    name = serializers.SerializerMethodField('_name')
    photo = serializers.SerializerMethodField('_photo')
    member = serializers.SerializerMethodField('_member')

    def _member(self, instance):
        if instance.member:
            return instance.member.pk
        return None

    def _name(self, instance):
        if instance.member:
            return instance.member.display_name()
        return instance.name

    def _photo(self, instance):
        if instance.member and instance.member.photo:
            f = instance.member.photo.file
            type = mimetypes.guess_type(f.name)[0]
            photo = ''.join(['data:{};base64,'.format(type),
                             b64encode(f.read()).decode()])
        else:
            filename = find_static_file('members/images/default-avatar.jpg')
            with open(filename, 'rb') as f:
                photo = ''.join(['data:image/jpeg;base64,',
                                 b64encode(f.read()).decode()])
        return photo

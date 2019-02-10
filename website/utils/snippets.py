"""Provides various utilities that are useful across the project"""
import hmac
from _sha1 import sha1
from base64 import urlsafe_b64decode, urlsafe_b64encode
from datetime import datetime

from django.conf import settings
from django.template.defaultfilters import urlencode
from django.utils import timezone
from pytz import InvalidTimeError
from rest_framework.exceptions import ParseError


def datetime_to_lectureyear(date):
    """Convert a :class:`~datetime.date` to the start of the lectureyear

    >>> from datetime import date, datetime, timezone
    >>> nov_23 = date(1990, 11, 7)
    >>> datetime_to_lectureyear(nov_23)
    1990
    >>> mar_2 = date(1993, 3, 2)
    >>> datetime_to_lectureyear(mar_2)
    1992

    Also works on :class:`~datetime.datetime`, but they need to be tz-aware:

    >>> new_year = datetime(2000, 1, 1, tzinfo=timezone.utc)
    >>> datetime_to_lectureyear(new_year)
    1999
    """

    if isinstance(date, timezone.datetime):
        date = timezone.localtime(date).date()
    sept_1 = timezone.make_aware(timezone.datetime(date.year, 9, 1))
    if date < sept_1.date():
        return date.year - 1
    return date.year


def create_google_maps_url(location, zoom, size):
    maps_url = (f"/maps/api/staticmap?"
                f"center={ urlencode(location) }&"
                f"zoom={ zoom }&size={ size }&"
                f"markers={ urlencode(location) }&"
                f"key={ settings.GOOGLE_MAPS_API_KEY }")

    decoded_key = urlsafe_b64decode(settings.GOOGLE_MAPS_API_SECRET)

    signature = hmac.new(decoded_key, maps_url.encode(), sha1)

    encoded_signature = urlsafe_b64encode(signature.digest())

    maps_url += f"&signature={encoded_signature.decode('utf-8')}"

    return "https://maps.googleapis.com" + maps_url


def _extract_date(param):
    """Extract the date from an arbitrary string"""
    if param is None:
        return None
    try:
        return timezone.make_aware(
                datetime.strptime(param, '%Y-%m-%dT%H:%M:%S'))
    except ValueError:
        return timezone.make_aware(datetime.strptime(param, '%Y-%m-%d'))


def extract_date_range(request, allow_empty=False):
    """Extract a date range from an arbitrary string"""

    default_value = ''
    if allow_empty:
        default_value = None

    try:
        start = _extract_date(request.query_params.get('start', default_value))
    except (ValueError, InvalidTimeError) as e:
        raise ParseError(detail='start query parameter invalid') from e

    try:
        end = _extract_date(request.query_params.get('end', default_value))
    except (ValueError, InvalidTimeError) as e:
        raise ParseError(detail='end query parameter invalid') from e

    return start, end

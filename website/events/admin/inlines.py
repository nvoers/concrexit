from django.contrib import admin

from events import models
from .forms import RegistrationInformationFieldForm
from pizzas.models import FoodEvent


class RegistrationInformationFieldInline(admin.TabularInline):
    """The inline for registration information fields in the Event admin."""

    form = RegistrationInformationFieldForm
    extra = 0
    model = models.RegistrationInformationField
    ordering = ("_order",)

    radio_fields = {"type": admin.VERTICAL}

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj is not None:
            count = obj.registrationinformationfield_set.count()
            formset.form.declared_fields["order"].initial = count
        return formset


class PizzaEventInline(admin.StackedInline):
    """The inline for pizza events in the Event admin."""

    model = FoodEvent
    exclude = ("end_reminder",)
    extra = 0
    max_num = 1

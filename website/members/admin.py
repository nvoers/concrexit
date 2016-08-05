"""
This module registers admin pages for the models
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from . import models


class MembershipInline(admin.StackedInline):
    model = models.Membership
    extra = 0


class MemberInline(admin.StackedInline):
    model = models.Member
    can_delete = False


class MembershipTypeListFilter(admin.SimpleListFilter):
    title = _('membership type')
    parameter_name = 'membership'

    def lookups(self, request, model_admin):
        return models.Membership.MEMBERSHIP_TYPES

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        queryset.prefetch_related('user__memberships')
        users = set()
        for user in queryset:
            try:
                if user.member.current_membership:
                    if user.member.current_membership.type == self.value():
                        users.add(user.pk)
            except models.Member.DoesNotExist:
                # The superuser does not have a .member object attached.
                pass
        return queryset.filter(pk__in=users)


class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline, MembershipInline)
    # FIXME include proper filter for expiration
    # https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    list_filter = (MembershipTypeListFilter,
                   'is_superuser',)
    # FIXME use nicer form
    # form = forms.AdminForm (base on ModelForm, reorder elements, etc).

admin.site.register(models.BecomeAMemberDocument)

# re-register User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

import os.path

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import (HttpResponseBadRequest, Http404,
                         HttpResponseForbidden, JsonResponse)
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.debug import (sensitive_variables,
                                           sensitive_post_parameters)

from sendfile import sendfile

from members.models import Member


@login_required
def styleguide(request):
    return render(request, 'singlepages/styleguide.html')


@sensitive_variables()
@sensitive_post_parameters()
@require_POST
@csrf_exempt
def wiki_login(request):
    apikey = request.POST.get('apikey')
    user = request.POST.get('user')
    password = request.POST.get('password')

    if apikey != settings.WIKI_API_KEY:
        return HttpResponseForbidden('{"status":"error","msg":"invalid key"}',
                                     content_type='application/json')
    if user is None or password is None:
        return HttpResponseBadRequest(
            '{"status":"error","msg":"Missing username or password"}',
            content_type='application/json')

    user = authenticate(username=user, password=password)
    if user is not None:
        try:
            memberships = [cmm.committee.wiki_namespace for cmm in
                           user.member.committeemembership_set.exclude(
                               until__lt=timezone.now().date())
                           .select_related('committee')
                           if cmm.committee.wiki_namespace is not None]
        except Member.DoesNotExist:
            memberships = []

        if user.has_perm('board_wiki'):
            memberships.append('bestuur')

        return JsonResponse({'status': 'ok',
                             'name': user.get_full_name(),
                             'mail': user.email,
                             'admin': user.is_superuser,
                             'msg': 'Logged in',
                             'committees': memberships})
    return JsonResponse({'status': 'error',
                         'msg': 'Authentication Failed'},
                        status=403)


@login_required
def styleguide_file(request, filename):
    path = os.path.join(settings.MEDIA_ROOT, 'styleguide')
    filepath = os.path.join(path, filename)
    if not (os.path.commonprefix([path, filepath]).startswith(path) and
            os.path.isfile(filepath)):
        raise Http404("File not found.")
    return sendfile(request, filepath, attachment=True)


@staff_member_required
def crash(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("This is not for you")
    raise Exception("Test exception")

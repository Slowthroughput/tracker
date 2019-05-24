from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dashboard

def index(request):
    latest_engagement_list = Dashboard.objects.order_by('-pub_date')[:5]
    context = {'latest_engagement_list': latest_engagement_list}
    return render(request, 'main/index.html/', context)

def view_engagement(request, engagement_id):
    try:
        engagement = Dashboard.objects.get(pk=engagement_id)
    except Dashboard.DoesNotExist:
        raise Http404('Engagement does not exist')
    return render(request, 'main/detail.html', {'engagement': engagement})

def view_host(request, engagment_id):
    return HttpResponse("Host Detail: %s." % engagment_id)

def view_creds(request, engagment_id):
    return HttpResponse("Credential: %s." % engagment_id)

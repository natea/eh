# Create your views here.
import sys, os, traceback
import settings
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpRequest
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from eh.furl.models import Furl, Tag


# build the main table & the entry for new elements (use backbone?)
# build the bookmarklet for submission client side

@login_required
def index(request):
    furls = request.user.furl_set.all()
    ctx = get_context(request, dict(furls=furls, description="All furls"))
    t = loader.get_template("furl/main.html")
    return HttpResponse(t.render(ctx))

@login_required
def add_link(request):
    """ pass in params: url (req), title (opt), tag(s) (comma sep, opt) """
    if request.POST:
        url    = request.POST['url']
        title  = request.POST.get('title','')
        raw_tags = request.POST.get('tags','')
        try:
            furl = Furl.objects.get(owner=request.user, url=url, title=title)
            res = 'Already saved url on %s' % furl.date_added
        except Furl.DoesNotExist:
            furl =  Furl(owner=request.user, url=url, title=title)
            furl.save()
            res = 'URL Saved!'
        # now lets roll through the tags:
        for t in raw_tags.split():
            try:
                t = t.lower()
                t = Tag.objects.get(owner=request.user, name=t)
            except Tag.DoesNotExist:
                t = Tag(owner=request.user, name=t)
                t.save()
            furl.tag_set.add(t)
            
        return HttpResponse(res)
    else:
        print request.GET['title']
        return render_to_response('furl/add.html', get_context(request))

@login_required
def send_adder(request):
    return render_to_response('furl/adder.js',get_context(request))

@login_required
def extras(request):
    return render_to_response('furl/extras.html', get_context(request))

@login_required
def tags(request):
    l = [ x for x in request.user.tag_set.all()]
    l.sort(key=lambda x: x.furl_count, reverse=True)
    return render_to_response('furl/tags.html', get_context(request, {'tags': l}))

@login_required
def get_tag(request, tag):
    description = "Tag %s" % tag
    tag = Tag.objects.get(owner=request.user, name=tag)
    furls = tag.furls.all()
    ctx = get_context(request, dict(furls=furls, description=description))
    t = loader.get_template("furl/main.html")
    return HttpResponse(t.render(ctx))
    

# util functions:
def get_context(request, d={}):
    r = RequestContext(request, d)
    r['FURL_ROOT'] = settings.FURL_ROOT
    return r
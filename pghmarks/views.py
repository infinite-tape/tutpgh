from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from pghmarks.models import Landmark
# For Advanced Section
from django.views.generic.list import ListView


def hello_world(request):
    '''
    If we were to hit this view with a web browser we would not
    see html content, instead the server would return a single text
    string "Hello, Pittsburgh!". In reality, this should be written as:

    return HttpResponse("Hello, Pittsburgh!", mimetype="text/plain")
    '''
    return HttpResponse("Hello, Pittsburgh!")

def landmark_list(request):
    '''
    Query the database using the Django ORM and return a list of
    all the Landmark objects. Pass this list off to the template
    for rendering into HTML and sending back to the browser.
    '''
    object_list = Landmark.objects.all()
    total_landmarks = Landmark.objects.count()
    return render_to_response('pghmarks/landmark_list.html',
                              {'object_list': object_list,
                               'total_landmarks': total_landmarks})

def landmark_detail(request, slug=None):
    '''
    Query the database using the Django ORM and return a single
    Landmark object per the given `slug`. Pass this object to the
    template for rendering into HTML and sending back to the
    browser.
    '''
    try:
        object = Landmark.objects.get(slug=slug)
    except Landmark.DoesNotExist:
        raise Http404
    return render_to_response('pghmarks/landmark_detail.html',
                              {'object': object})

class LandmarkListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super(LandmarkListView, self).get_context_data(*args, **kwargs)
        context['landmark_count'] = Landmark.objects.count()
        return context

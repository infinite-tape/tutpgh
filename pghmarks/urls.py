from django.conf.urls import patterns, include, url
from pghmarks.views import landmark_list, landmark_detail

# For Advanced Section
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from pghmarks.views import LandmarkListView
from pghmarks.models import Landmark
from pghmarks.forms import LandmarkForm


urlpatterns = patterns(
    '',
    # Function list view
    url(r'^$', landmark_list, name='landmark_list'),

    # Function detail view
    url(r'^landmark/(?P<slug>[\w-]+)/$', landmark_detail,
        name='landmark_detail'),

    # Class-based, built-in generic ListView
    #
    # The built-in Django generic views are all constructed
    # using the pattern below. You must call as_view() method
    # to get a usable version of each generic view class. This
    # method takes arguments that configure the view.
    #
    # In the below example, we're passing in Landmark as the
    # `model` kwarg. ListView will use whatever is defined
    # as `model` to automatically provide context data to the
    # template in an {{ object_list }} context variable.
    #
    # Essentially this does `model.objects.all()` and passes
    # the result to our template.
    #
    # Instead of model, you can pass-in `queryset` and ListView
    # will use that instead
    #
    # ListView.as_view(queryset=Landmark.objects.filter(neighborhood__name='Oakland')
    #
    url(r'^list1/$', ListView.as_view(
            model=Landmark,
            template_name='pghmarks/landmark_list.html'),
        name='landmark_list'),

    # Class-based, customized generic ListView subclass (LandmarkListView)
    #
    # See `LandmarkListView` sub-class in this app's views.py for
    # more details.
    #
    url(r'^list2/$', LandmarkListView.as_view(
            template_name='pghmarks/landmark_list.html')),    

    # Class-based, built-in generic DetailView
    url(r'^landmark/(?P<slug>[\w-]+)/$', DetailView.as_view(
            model=Landmark,
            template_name='pghmarks/landmark_detail.html'),
        name='landmark_detail'),

    # Class-based, built-in generic CRUD view (CreateView)
    #
    # Provide a form for creating new Landmarks on the website. Uses
    # a default ModelForm for the model specified, which includes
    # all the editable model fields in the form HTML.
    #
    url(r'^create/$', CreateView.as_view(
            model=Landmark,
            success_url='/'),
        name='landmark_create')

    # Class-based, built-in generic CRUD view with custom ModelForm
    #
    # Instead of using the default, automatically generated ModelForm,
    # use a customized version we wrote in forms.py
    #
    url(r'^create2/$', CreateView.as_view(
            form_class=LandmarkForm,
            model=Landmark,
            success_url='/'),
        name='landmark_create')
    
    )

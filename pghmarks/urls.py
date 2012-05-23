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
    url(r'^$', landmark_list, name='landmark_list'),
    url(r'^landmark/(?P<slug>[\w-]+)/$', landmark_detail,
        name='landmark_detail'),

    # For Advanced Section
    # url(r'^$', ListView.as_view(
    #         model=Landmark,
    #         template_name='pghmarks/landmark_list.html'),
    #     name='landmark_list'),

    # url(r'^$', LandmarkListView.as_view(
    #         template_name='pghmarks/landmark_list.html')),    

    # url(r'^landmark/(?P<slug>[\w-]+)/$', DetailView.as_view(
    #         model=Landmark,
    #         template_name='pghmarks/landmark_detail.html'),
    #     name='landmark_detail'),

    # url(r'^create/$', CreateView.as_view(
    #         model=Landmark,
    #         success_url='/'),
    #     name='landmark_create')

    # url(r'^create/$', CreateView.as_view(
    #         form_class=LandmarkForm,
    #         model=Landmark,
    #         success_url='/'),
    #     name='landmark_create')
    
    )

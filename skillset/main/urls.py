from django.conf.urls import url

from . import views

urlpatterns = [
#    url(r'', views.home, name='home'),
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^data/$', views.DataPageView.as_view(), name='data'),  # Add this URL pattern
]

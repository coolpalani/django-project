from django.conf.urls import url, include
from django.contrib import admin
from . import views
from main.views import HomePageView, UserCreateView

#urlpatterns = [
#    url(r'', views.home, name='home'),
#    url(r'', UserList.as_view() ),
#    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
#    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
#    url(r'^data/$', views.DataPageView.as_view(), name='data'),  # Add this URL pattern
#]

urlpatterns = (

    url(r'', HomePageView.as_view(), name='homepage'),
    url(r'create/$', UserCreateView.as_view(), name='create_user'),


)

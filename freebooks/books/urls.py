from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^books/$', views.IndexView.as_view(), name='index'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^books/(?P<book_id>[0-9]+)/download/$', views.pdf_download, name='download'),
]


from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.init),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^amadon$', views.index),
    url(r'^process$', views.process),
    url(r'^amadon/checkout$', views.checkout),

]  
from django.conf.urls import url

from . import views
# To call the view, we need to map it to a URL - and for this we need a URLconf
urlpatterns = [
    url(r'^$', views.index, name='index'),

]


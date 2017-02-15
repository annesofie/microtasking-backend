from django.conf.urls import include, url
from django.contrib import admin

from base.urls import router as base_router

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# The include() function allows referencing other URLconf
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(base_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

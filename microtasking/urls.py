from django.conf.urls import include, url
from django.contrib import admin

from base.urls import router as base_router
from survey_results.urls import router as survey_result_router

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# The include() function allows referencing other URLconf
from base.views import BuildingElementsView

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(base_router.urls)),
    url(r'^result/', include(survey_result_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/buildings/layers/$', BuildingElementsView.as_view())
]

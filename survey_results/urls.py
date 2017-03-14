from rest_framework import routers

from survey_results import views

router = routers.DefaultRouter()
router.register(r'tasksurvey', views.TasksurveyViewSet)
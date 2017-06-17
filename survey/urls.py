from django.conf.urls import url

from .views import SurveyCreate, SurveyList

urlpatterns = [
    url(r'^$', SurveyCreate.as_view(), name='new'),
    url(r'^surveys', SurveyList.as_view(), name='list'),

]
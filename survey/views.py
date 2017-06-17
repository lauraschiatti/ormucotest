# -*- coding: utf-8 -*-

from django.views.generic import CreateView,  ListView
from survey.models import Survey
from survey.forms import SurveyForm

class SurveyCreate(CreateView):
    model = Survey
    form_class = SurveyForm
    template = 'survey/survey_form.html'
    success_url = 'surveys'


class SurveyList(ListView):
    model = Survey
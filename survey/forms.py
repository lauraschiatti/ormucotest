from django.forms import ModelForm, TextInput, ChoiceField, Select

from .models import Survey

class SurveyForm(ModelForm):
    animal = ChoiceField(
        label='Animal',
        choices=[('cats', 'Cats'),('dogs', 'Dogs')],
        widget=Select(attrs={'class': 'form-control form-control-lg custom-select form-control-danger'})
    )

    class Meta:
        model = Survey
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control form-control-lg form-control-danger' }),
            'favorite_color': TextInput(attrs={'class': 'form-control', 'type': 'color', 'value': '#563d7c'})
        }

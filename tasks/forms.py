from .models import Task
from django.forms import ModelForm, TextInput, Textarea, BooleanField, CheckboxInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description', 'completed']
        widgets = {
            'title': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Напишите Свою Задачу"
            }),
            'description': Textarea(attrs={
                "class": "form-control",
                "placeholder": "Описание"
                }),

            'completed': CheckboxInput(attrs={
                "class": "form-check-input "
                  })   
        }


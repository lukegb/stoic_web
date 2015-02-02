from django import forms

from .models import QuestionsLive

class QLForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QLForm, self).__init__(*args, **kwargs)

        self.fields['ip'].required = False
        self.fields['user_agent'].required = False

    class Meta:
        model = QuestionsLive

        fields = ['name', 'email', 'question', 'be_there', 'ip', 'user_agent']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'question': forms.Textarea(attrs={'placeholder': 'Question'})
        }
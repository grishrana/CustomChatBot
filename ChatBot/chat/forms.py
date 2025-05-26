from django import forms
from .models import Prompts


class ConversationForm(forms.Form):
    prompt = forms.CharField(max_length=500, label="prompt")

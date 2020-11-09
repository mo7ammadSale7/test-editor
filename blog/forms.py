from django.forms import ModelForm

from .models import Article

class TextEditForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text',)
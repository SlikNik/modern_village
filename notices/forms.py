from django import forms
from notices.models import Notice


class AddNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('type_of', 'title', 'body', 'is_urgent', 'price')

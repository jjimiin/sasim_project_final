from django import forms
from .models import Contact_Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Contact
        fields = ('title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}),
            'text': forms.Textarea(
                attrs={'placeholder': '문의할 내용을 입력하세요'}),
        }


class replyForm(forms.ModelForm):
    class Meta:
        model = Contact_Contact
        fields = ('reply',)

        widgets = {
            'reply': forms.Textarea(
                attrs={'placeholder': '답변을 입력하세요'}),
        }


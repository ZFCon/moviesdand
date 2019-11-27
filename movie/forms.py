from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(label = '', max_length=330, widget = 
    forms.TextInput(attrs = {
        'class': "form-control", 
        'placeholder': "Write your comment here."
        }))
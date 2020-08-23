from django import forms


class ShrnkForm(forms.Form):
    og_url = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'type':"url",'maxlength':"200", 'id':"og_url",'name':'og_url','class':'input',
    }))
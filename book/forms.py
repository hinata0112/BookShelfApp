from django import forms

# 検索機能
class SearchForm(forms.Form):
    words = forms.CharField(
        label = ' ',
        max_length = 50,
        widget = forms.TextInput(attrs = {
            'class':'form-control me-2', 
            'placeholder':'タイトルで検索', 
        })
    )
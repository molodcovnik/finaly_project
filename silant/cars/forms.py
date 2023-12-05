from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_field'].widget.attrs['placeholder'] = 'Зав. № машины'
        self.fields['search_field'].label = ''
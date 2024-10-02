from django import forms

class UploadFileForm(forms.Form):

    excel_file = forms.FileField()
    files = forms.FileField(widget=forms.ClearableFileInput(), required=False)
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    sender_age = forms.IntegerField()
    cc_myself = forms.BooleanField(required=False)

    def clean_sender_age(self):
        data = self.cleaned_data['sender_age']
        if data < 21:
            raise forms.ValidationError("You are not supposed to write email ")
            # Always return a value to use as the new cleaned data, even if
            # this method didn't change it.
        return data
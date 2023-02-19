from django import forms


class Profile(forms.Form):

    first_name = forms.CharField(label ="First Name", max_length=200)
    last_name = forms.CharField(label = "Last Name",max_length=200)


class ContactForm(forms.Form):

    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget= forms.Textarea())
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    
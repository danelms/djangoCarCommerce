from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label="")

class PurchaseForm(forms.Form):
    name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=100)
    phone = PhoneNumberField(label="Contact number")
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label="")
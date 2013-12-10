from django import forms 

class ContactForm(forms):
	subject = forms.CharFields()
	email = forms.EmailFields()
	message  = forms.CharFields()

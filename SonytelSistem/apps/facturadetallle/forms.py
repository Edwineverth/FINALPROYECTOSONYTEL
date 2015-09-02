from django import forms
from django.contrib.auth.forms import UserCreationForm
class detalleFacturaForm(UserCreationForm):
	cantidad=forms.IntegerField()
	preciou=forms.DecimalField()
	preciot=forms.DecimalField()
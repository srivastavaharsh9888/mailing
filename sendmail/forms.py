from django import forms

class Feedback(forms.Form):
	Email=forms.EmailField(max_length=100)																																																																									
	subject=forms.CharField(max_length=1500,required=False)
	matter=forms.CharField(widget=forms.Textarea())

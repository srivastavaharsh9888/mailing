from django.shortcuts import render,redirect
from django.core.mail import EmailMessage	

from sendmail.forms import Feedback

def home(request):
	message=""
	feedback_form=Feedback()
	if request.method=='POST':
		feedback_form=Feedback(request.POST)
		if feedback_form.is_valid():
			to_user=feedback_form.cleaned_data.get('Email')
			mail_sub=feedback_form.cleaned_data.get('subject')
			mail_mat=feedback_form.cleaned_data.get('matter')
			email = EmailMessage(
			mail_sub, mail_mat, to=[to_user])
			email.send()
			feedback_form=Feedback()
			message="Thanks for the feedback "+  to_user+"."
			#return render(request,'sendmail/index.html',{'form':feedback_form,'message':message})
			return render(request,'sendmail/index.html',{'form':feedback_form,'message':message})
		else:
			feedback_form=Feedback()
			return render(request,'sendmail/index.html',{'form':feedback_form,'message':message})
			
	return render(request,'sendmail/index.html',{'form':feedback_form,'message':message})

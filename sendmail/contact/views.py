from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def contact_form(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = "To: "+ email + "\n"
        message += "Receiver Name: "+ name + "\n\r\n\r"
        message += "-------------------------------------------------------"
        message += "\n\r\n\r"

        message += request.POST['message']

        try:
            send_mail(
                'New Message - '+ name,# subject,
                message,#message
                email,# from email
                [str(email)],# to email,
                #fail_silently=False
            )
            context = {'mail_response':True}
        except Exception as err:
            raise err

    return render(request,'contact_information.html',context)

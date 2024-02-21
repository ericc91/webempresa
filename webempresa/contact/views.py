from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .form import ContactForm

# Create your views here.
def contact(request):       
    if request.method == "POST":
       contact_form = ContactForm(request.POST)
       if contact_form.is_valid():
         name = request.POST.get('name','')
         email = request.POST.get('email','')
         content = request.POST.get('content','')
        #enviamos el correo y redireccionamos
         email = EmailMessage(
            subject="La Caffettiera: Nuevo mensaje de contacto",
            body=f"De {name} <{email}>\n\nEscribió:\n\n{content}",
            from_email="no-contestar@gmail.com",
            to=["eritovaradero@gmail.com"],
            reply_to=[email],
            headers={'from': "no_contestar@gmail.com"}
         )
         try:
          email.send()
          #todo ha ido bien, redireccionamos a OK
          return redirect(reverse('contact')+"?ok")
         except:
            #algo no ha ido bien, redireccionamos a Fail
            return redirect(reverse('contact')+"?fail")
    else:
     contact_form = ContactForm()
    return render(request,'contact/contact.html', {'form':contact_form})
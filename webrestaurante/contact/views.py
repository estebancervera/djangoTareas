from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # mandar correo
            send_mail(
                'Mensaje de ' + name, # Asunto
                content, # Mensaje
                email, # De quien
                ['andoni_rdgz@hotmail.com', 'andoni_rdgz@outlook.com', 'arielito66@hotmail.com'], # Para quien
            )

            return redirect(reverse('contact') + '?ok')



    return render(request, 'contact/contact.html', {'form': contact_form})

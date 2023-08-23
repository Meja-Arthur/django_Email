from django.shortcuts import render, redirect
from.forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    
    
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      
      html = render_to_string('contactform.html',{
        'name': name,
        'email': email,
        'message': message
      })
      
      send_mail('The contact form subject','this is the message',
                'nonreply@gfanuk.com',
                ['arthurogembo@gmail.com'], html_message=html)
      return redirect('index')
      
  else:
    form = ContactForm()
        
   
  return render(request, 'index.html',{
          'form': form  
        })

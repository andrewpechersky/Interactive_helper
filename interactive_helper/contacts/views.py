from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from .models import Contact

# Create your views here.
@login_required
def add_contact(request):
    form_contact = ContactForm(instance=Contact())
    if request.method == "POST":
        form_contact = ContactForm(request.POST, instance=Contact())
        if form_contact.is_valid():
            form_contact.save()
            return redirect(to='contacts:contacts')

    return render(request, 'contacts/add_contact.html', context={'form_contact': form_contact})

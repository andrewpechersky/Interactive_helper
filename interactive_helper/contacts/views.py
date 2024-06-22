from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


# Create your views here.
@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


@login_required
def add_contact(request):
    contact_form = ContactForm(instance=Contact())
    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance=Contact())
        if contact_form.is_valid():
            contact_form.save()
            fullname = contact_form.cleaned_data['fullname']
            messages.success(request, message=f'You´ve successfully added {fullname}')
            return redirect(to='contacts:contact_list')
        else:
            messages.error(request, message="Error")
    return render(request, 'contacts/add_contact.html', context={'form': contact_form})


@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact = contact_form.save()
            return redirect('contacts:contact_list')
    else:
        contact_form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', context={'form': contact_form})


@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return render(request, 'contacts/delete_contact.html')

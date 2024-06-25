from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .forms import ContactForm
from .models import Contact


# Create your views here.
@login_required
def contact_list(request):
    query = request.GET.get('query')

    if query:
        contacts = Contact.objects.filter(fullname__icontains=query)
    else:
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
            messages.success(request, f'You have successfully added {fullname}')
            return redirect('contacts:contact_list')
        else:
            messages.error(request, "Error")
    return render(request, 'contacts/add_contact.html', {'form_contact': contact_form})


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
    if request.method == "POST":
        contact.delete()
        messages.success(request, f'Contact {contact.fullname} has been deleted.')
        return redirect('contacts:contact_list')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})


@login_required
def upcoming_birthdays_list(request):
    days  = int(request.GET.get('days'))
    today = timezone.now()
    future_date = today + timedelta(days=days)
    upcoming_contacts = Contact.objects.filter(birth_date__day=future_date.day, birth_date__month=future_date.month)
    return render(request, 'contacts/search_result.html', {'upcoming_contacts': upcoming_contacts, 'days': days})


@login_required
def search_by_birthday_range(request):
    # if request.method == 'GET':
    start_date = timezone.now()
    end_date   = start_date + timedelta(request.GET.get('days'))
    contacts   = Contact.objects.filter(birthday__range=[start_date, end_date])
        # return render(request, 'search_result.html', {'results': results})
    # else:
    #     form = ContactForm(initial={
    #         'start_date': datetime.today().date(),
    #         'end_date': (datetime.today() + timedelta(days=30)).date()
        # })
    return render(request, 'search_result.html', {'contacts': contacts})

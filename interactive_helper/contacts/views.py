from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .forms import ContactForm
from .models import Contact
from datetime import date, timedelta

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


def upcoming_birthdays_list(request):
    days = request.GET.get('days')
    try:
        days = int(days)
    except (TypeError, ValueError):
        days = 365  # За замовчуванням шукаємо на наступні 365 днів

    # Отримуємо всі контакти з бази даних
    contacts = Contact.objects.all()

    # Отримуємо сьогоднішню дату
    today = date.today()

    # Визначаємо цільну дату для пошуку
    target_date = today + timedelta(days=days)

    # Ініціалізуємо порожній список для майбутніх днів народження з даними контактів
    upcoming_birthdays = []

    # Збираємо всі майбутні дні народження з даними контактів
    for contact in contacts:
        if contact.born_date:
            # Визначаємо дату народження для поточного року
            birthday_this_year = date(today.year, contact.born_date.month, contact.born_date.day)

            # Перевіряємо, чи дата народження цього року ще не минула і входить в потрібний період
            if today <= birthday_this_year <= target_date:
                upcoming_birthdays.append({
                    'contact': contact,
                    'birthday_date': birthday_this_year,
                })

    # Сортуємо список за датами народжень
    upcoming_birthdays.sort(key=lambda x: x['birthday_date'])

    return render(request, 'contacts/upcoming_birthdays_list.html', {
        'upcoming_birthdays': upcoming_birthdays,
        'days': days,
        'target_date': target_date,
    })
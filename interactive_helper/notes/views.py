from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.db import IntegrityError
from django.contrib import messages

from .forms import TagForm, NoteForm

from .models import Tag, Note


# Create your views here.
<<<<<<< HEAD
@login_required
=======
>>>>>>> 5c0fd8c183086e956fdcce7b8b08f99ae901e3f2
def main(request):
    query = request.GET.get('q')
    tag_query = request.GET.get('tag')
    if request.user.is_authenticated:
        if query:
            notes = Note.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query),
                user=request.user
            ).distinct()
        elif tag_query:
            notes = Note.objects.filter(
                tags__name__icontains=tag_query,
                user=request.user
            ).distinct()
        else:
            notes = Note.objects.filter(user=request.user)
    else:
        notes = []
    return render(request, 'notes/index.html', {"notes": notes, "query": query, "tag_query": tag_query})


@login_required
def tag(request):
    tags = Tag.objects.filter(user=request.user).all()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data['name']
            existing_tag = Tag.objects.filter(name=tag_name, user=request.user).first()
            if existing_tag:
                messages.error(request, f"Tag '{tag_name}' already exists.")
            else:
                tag = form.save(commit=False)
                tag.user = request.user
                try:
                    tag.save()
                    messages.success(request, f"Tag '{tag_name}' added successfully.")
                    return redirect('notes:tag')  # Redirect to the same page to clear the form
                except IntegrityError:
                    messages.error(request, "An error occurred while saving the tag.")
    else:
        form = TagForm()

    return render(request, 'notes/tag.html', {'form': form, 'tags': tags})

@login_required
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id, user=request.user)
    tag.delete()
    messages.success(request, f"Tag '{tag.name}' deleted successfully.")
    return redirect('notes:tag')

@login_required
def note(request):
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), user=request.user)
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='notes:index')
        else:
            return render(request, 'notes/add_notes.html', {"tags": tags, 'form': form})

    return render(request, 'notes/add_notes.html', {"tags": tags, 'form': NoteForm()})


@login_required
def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    return render(request, 'notes/detail.html', {"note": note})

@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id, user=request.user).update(done=True)
    return redirect(to='notes:index')


@login_required
def delete_note(request, note_id):
    Note.objects.get(pk=note_id, user=request.user).delete()
    return redirect(to='notes:index')


@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note_form = NoteForm(request.POST, instance=note)
        if note_form.is_valid():
            note = note_form.save()
            return redirect('notes:index')
    else:
        note_form = NoteForm(instance=note)
    return render(request, 'notes/edit_notes.html', context={'form': note_form})


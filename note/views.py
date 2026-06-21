from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib import messages

def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'note/notes_list.html', {'notes':notes})

def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note/notes_detail.html', {'note':note})

def notes_delete(request, pk):
    note = get_object_or_404(Note,pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'The Note has been succesfully deleted')
        return redirect('notes:notes_list')
    else:
        return render(request, 'note/delete_confirmation_page.html', {'note': note})
        
def notes_create(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The note has been successfully created')
            return redirect('notes:notes_list')
        else:
            messages.error(request, 'Please enter all the details in valid format.')
    return render(request, 'note/notes_create.html', {'form':form})


def notes_edit(request,pk):
    note = get_object_or_404(Note, pk = pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request,'The note has been updated')
            return redirect('notes:notes_list')
    else:
        form =NoteForm(instance=note)
    return render(request,'note/notes_edit.html', {'form':form})
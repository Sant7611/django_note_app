from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm, UserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='notes:login_notes')
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

def register_notes(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Logged In successfully")
            print("This reached register notes")
            return redirect('notes:notes_list')
        else:
            print(form.errors)
            messages.error(request, "The input is not valid")
            print("The user is nto registered")
    else:
        form = UserForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_notes(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            print("This is before user ")
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully logged in')
                return redirect('notes:notes_list')
            else:
                messages.error(request, "The user is not registered yet.")
        else:
            messages.error(request, "password or username is missing...")
    
    return render(request, 'accounts/login.html')

def logout_views(request):
    logout(request)
    messages.success(request, "You have been successfullly logged out")
    return redirect('notes:login_notes')
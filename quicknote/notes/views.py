from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


from .models import Notes
from .api import get_all_list


@csrf_exempt
def create_note(request):
    if request.method == 'POST':
        
        try:
            note_data = json.loads(request.body.decode('utf-8'))  # Parse the JSON data
        
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data") 

        userName = note_data.get("userName")
        textContent = note_data.get("textContent")
        title = note_data.get("title")

        note = Notes(userName=userName, title=title, textContent=textContent)

        try:
            note.save()
            response_data = {"status": "success", "message": "Note saved to the database"}
        except Exception as e:
            response_data = {"status": "failure", "message": str(e)}

        return JsonResponse(response_data)

    return HttpResponse("Invalid Request") 

def edit_note(request, note_id):
    note = get_object_or_404(Notes, noteId=note_id)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NotesForm(instance=note)
    return render(request, 'edit_note.html', {'form': form, 'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Notes, noteId=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'delete_note.html', {'note': note})

def notes_list1(request):
    notes = Notes.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})


def notes_list(request):
    return render(request, 'notes.html',{"notes":get_all_list()})
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


@login_required
def create_note(request):
    if request.method == 'POST':
        
        try:
            note_data = json.loads(request.body.decode('utf-8'))  # Parse the JSON data
        
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data") 

        userName = request.user.username
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

@login_required
def edit_note(request):

    if request.method == "POST":
        try:
            edit_note = json.loads(request.body.decode('utf-8')) # Parse the JSON data
            
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data request")

        noteId = edit_note.get('id')
        textContent = edit_note.get('textcontent')

        if noteId:
                try:    
                    note = Notes.objects.get(noteId=noteId)
                    note.textContent = textContent
                    note.save()
                    return JsonResponse({'message': 'Note Updated successfully'})
                except Notes.DoesNotExist:
                    return JsonResponse({'error': 'Note not found'}, status=404)
        
    
    return JsonResponse({'error': 'Note ID not provided'}, status=400)

@login_required
def delete_note(request):
    if request.method == "DELETE":
        try:
            note_id = json.loads(request.body.decode('utf-8')).get("id") # Parse the JSON data
            
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data request") 

        if note_id:
            try:    
                note = Notes.objects.get(noteId=note_id)
                note.delete()
                return JsonResponse({'message': 'Note deleted successfully'})
            except Notes.DoesNotExist:
                return JsonResponse({'error': 'Note not found'}, status=404)
        else:
            return JsonResponse({'error': 'Note ID not provided'}, status=400)
        
    return JsonResponse({'error': 'Not Valid request'}, status=400)

@login_required    
def notes_list(request):
    username = request.user.username
    return render(request, 'notes.html',{"notes":get_all_list(username)})
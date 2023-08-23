from .models import Notes

def get_all_list(username):
    # Retrieve all notes of user from the database
    notes = Notes.objects.filter(userName=username)
    return notes

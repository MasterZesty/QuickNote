from .models import Notes

def get_all_list():
    notes = Notes.objects.all()  # Retrieve all notes from the database
    return notes

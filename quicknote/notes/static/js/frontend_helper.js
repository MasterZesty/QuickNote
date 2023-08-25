//delete note called when user give confrimation to delete note
function sendDeleteRequest(noteId) {

    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get the CSRF token from the DOM

    // console.log("note id ",noteId);
    var url = "http://127.0.0.1:8000/notes/delete/";
    var data = JSON.stringify({ id: noteId });

    fetch(url, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken // Make sure csrfToken is defined
        },
        body: data
    })
    .then(response => response.text())
    .then(result => {
        // console.log(result);
        // Handle success: Remove the note card from the DOM
        var noteCard = document.getElementById(noteId);
        // console.log("getElementById",noteCard);
        if (noteCard) {
            noteCard.remove();

            // Remove the modal backdrop
            document.querySelector('.modal-backdrop').remove();
        }

    })
    .catch(error => {
        console.error("Error deleting note", error);
    });
}



//edit note called when user updates note
function sendEditRequest(noteId) {

    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get the CSRF token from the DOM

    var textarea_id = "textContent_" + noteId;
    var note_content =  document.getElementById(textarea_id).value

    // console.log("Updated content ",note_content);
    // console.log("note id ",noteId);

    var url = "http://127.0.0.1:8000/notes/edit/";
    var data = JSON.stringify({ id: noteId , textcontent:note_content});

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken // Make sure csrfToken is defined
        },
        body: data
    })
    .then(response => response.text())
    .then(result => {
        // console.log(result);

        var noteCard = document.getElementById(noteId);
        // console.log("getElementById",noteCard);
        
        if (noteCard) {

            noteCard.remove();

            // Remove the modal backdrop
            document.querySelector('.modal-backdrop').remove();
        }

        // Handle success: add the updated note card to the DOM

        // for temp reload page
        location.reload();
        }
        
        )
    .catch(error => {
        console.error("Error deleting note", error);
    });
}





//create note called when user create note
function sendCreateRequest() {

    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get the CSRF token from the DOM

    var note_title = document.getElementById("noteTitle").value
    var note_content =  document.getElementById("noteTextContent").value

    // console.log("noteTitle",note_title);
    // console.log("noteTextContent",note_content);

    var url = "http://127.0.0.1:8000/notes/create/";
    var data = JSON.stringify({ title: note_title , textContent:note_content});

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken // Make sure csrfToken is defined
        },
        body: data
    })
    .then(response => response.text())
    .then(result => {
        // console.log(result);

        var noteSave = document.getElementById("create_staticBackdrop");
        // console.log("getElementById",noteSave);
        
        if (noteSave) {

            noteSave.remove();

            // Remove the modal backdrop
            document.querySelector('.modal-backdrop').remove();
        }

        // Handle success: add the updated note card to the DOM

        // for temp reload page
        location.reload();
        }
        
        )
    .catch(error => {
        console.error("Error deleting note", error);
    });
}


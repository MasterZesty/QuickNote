//delete note called when user give confrimation to delete note
function sendDeleteRequest(noteId) {
    // console.log("note id ",noteId);
    var url = "http://127.0.0.1:8000/notes/delete/";
    var data = JSON.stringify({ id: noteId });

    fetch(url, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            // "X-CSRFToken": csrfToken // Make sure csrfToken is defined
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
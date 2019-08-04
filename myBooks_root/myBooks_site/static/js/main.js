const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
if (document.getElementById("add_book_form_button")) {
    document.getElementById("add_book_form_button").disabled = true;
}

function showImportFromGb() {
    document.getElementById("add_book_form").style.display = "none";
    document.getElementById("import_from_gb_button").disabled = true;
    document.getElementById("import_from_gb").style.display = "block";
    document.getElementById("add_book_form_button").disabled = false;
}

function showAddBookForm() {
    document.getElementById("import_from_gb").style.display = "none";
    document.getElementById("add_book_form").style.display = "block";
    document.getElementById("import_from_gb_button").disabled = false;
    document.getElementById("add_book_form_button").disabled = true;
}

setTimeout(function() {
    $('.message').fadeOut('slow');
}, 3000);

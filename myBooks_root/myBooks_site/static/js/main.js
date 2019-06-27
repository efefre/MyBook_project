const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

function showImportFromGb() {
    document.getElementById("add_book_form").style.display = "none";
    document.getElementById("import_from_gb").style.display = "block";
}

function showAddBookForm() {
    document.getElementById("import_from_gb").style.display = "none";
    document.getElementById("add_book_form").style.display = "block";
}

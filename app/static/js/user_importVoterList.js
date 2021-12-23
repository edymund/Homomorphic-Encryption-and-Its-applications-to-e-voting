
function showname(){
    // var my_file_name = document.getElementById('myFile').files[0];
    var my_file_name = document.getElementById('myFile').files[0];
    document.getElementById('voter-list-tb').value = my_file_name.name;
}

function openfile(){
    document.getElementById('myFile').click();
}

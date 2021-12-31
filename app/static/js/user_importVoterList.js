
function showname(){
    // var my_file_name = document.getElementById('myFile').files[0];
    var my_file_name = document.getElementById('myFile').files[0];
    document.getElementById('voter-list-tb').value = my_file_name.name;
}

function openfile(){
    document.getElementById('myFile').click();
}

function fillTA(voter){
    var temp = "";
    for (let i = 0; i < voter.length; i++) {
        temp += voter[i] + "\n";
      }
    document.getElementById("allVoter").value = temp;
}
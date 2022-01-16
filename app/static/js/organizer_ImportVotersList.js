
function showname(){
    // var my_file_name = document.getElementById('myFile').files[0];
    var my_file_name = document.getElementById('myFile').files[0];
    document.getElementById('voter-list-tb').value = my_file_name.name;
}

function openfile(){
    document.getElementById('myFile').click();
}


function imgclick(){
    var modal = document.getElementById("myModal");
    var img = document.getElementById("myImg");
    var modalImg = document.getElementById("imgVL");
    var captionText = document.getElementById("caption");
    modal.style.display = "block";
    modalImg.src = img.src;
    captionText.innerHTML = "voter list sample";
  }
  


// When the user clicks on <span> (x), close the modal
function spanclose() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}


function fillTA(voter){
    var temp = "";
    for (let i = 0; i < voter.length; i++) {
        temp += voter[i] + "\n";
      }
    document.getElementById("allVoter").value = temp;
}
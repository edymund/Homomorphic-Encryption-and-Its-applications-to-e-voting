var rej_clicked = false;
function reject() {
    if (rej_clicked === false){
        document.getElementById("feedback").hidden  = false;
        document.getElementById("rejectBtn").hidden  = false;
        document.getElementById("feedback").required= true;
        rej_clicked = true;
    }
    else if (rej_clicked === true){
        document.getElementById("feedback").hidden  = true;
        document.getElementById("rejectBtn").hidden  = true;
        document.getElementById("feedback").required = false;
        rej_clicked = false;
    }
  }

function enable_submit(){
    if (document.getElementById("feedback").value.trim()  != "") {
        document.getElementById("rejectBtn").disabled  = false;
    }
    else{
        document.getElementById("rejectBtn").disabled  = true;
    }
}
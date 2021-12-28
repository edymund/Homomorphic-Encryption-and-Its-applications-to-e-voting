var confirmed = false;
function displayPopup(){
	
	if(!confirmed){
		document.querySelector('.bg-modal').style.display = 'flex';
		return false;
	} else {
		return true;
	}
	

}

function closePopup(){
	document.querySelector('.bg-modal').style.display = 'none';
}

function submitvote(){
	confirmed = true;
	document.getElementById("mainform").submit();
}

window.onload=function(){
	var buttonPopup = document.getElementById("popup");
	var buttonclose = document.getElementById("cancel");
	var submitbutton = document.getElementById("confirm");
	buttonPopup.addEventListener('click', displayPopup,false);
	buttonclose.addEventListener('click', closePopup,false);
	submitbutton.addEventListener("click",submitvote,false)

}


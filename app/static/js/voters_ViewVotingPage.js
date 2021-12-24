
function displayPopup(){
	
	document.querySelector('.bg-modal').style.display = 'flex';

}

function closePopup(){
	document.querySelector('.bg-modal').style.display = 'none';
}

window.onload=function(){
	var buttonPopup = document.getElementById("popup");
	var buttonclose = document.getElementById("close");
	buttonPopup.addEventListener('click', displayPopup,false);

	buttonPopup.onload=function(){
		buttonclose.addEventListener('click', closePopup,false);
	}
}

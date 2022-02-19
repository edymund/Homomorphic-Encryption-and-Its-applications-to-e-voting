window.onload = function () {
	var elem = document.getElementById("display-image");
	if ((elem.getAttribute("src") != "/") && (elem.getAttribute("src") != "")) 
	{
		document.getElementById("display-image").style.display = "block";
	}
};

function handleImageUpload() {
	var image = document.getElementById("candidateImage").files[0];

	var reader = new FileReader();

	reader.onload = function (e) {
		document.getElementById("display-image").src = e.target.result;
		document.getElementById("display-image").style.display = "block";
	};

	reader.readAsDataURL(image);
}

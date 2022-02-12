function downloadKey(filename, elId, mimeType) {
	var elHtml = document.getElementById(elId).innerHTML;
	var link = document.createElement("a");
	mimeType = mimeType || "text/plain";

	link.setAttribute("download", filename);
	link.setAttribute(
		"href",
		"data:" + mimeType + ";charset=utf-8," + encodeURIComponent(elHtml)
	);
	link.click();
}

function downloadKeys() {
	downloadKey('public_key', 'publickey', 'text/plain');
	downloadKey('secret_key', 'secretkey', 'text/plain');
}
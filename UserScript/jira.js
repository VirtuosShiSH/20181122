var issueId ="";
var myInput=document.body.appendChild(document.createElement("div"));
//var a = document.createTextNode("");


myInput.style.color ="#12006f";
myInput.style.backgroundColor ="#0037ffb5";
//myinput1.appendChild(a);

myInput.style.top = "10px";
myInput.style.left = "102px";
myInput.style.width = "0%";
myInput.style.height = "0%";
myInput.style.fontSize = "400px";
myInput.style.position = "fixed";
myInput.style.textAlign = "center";
myInput.style.marginTop = "320px";

//var myInput = document.body.appendChild(myinput1);

$(document).on("keydown", function (e) {
	var keyCode = e.keyCode || e.which;
	if (keyCode >= 96 && keyCode <= 105) {
		// Numpad keys
		keyCode -= 48;
	}
	if(isNaN(String.fromCharCode(keyCode))==false){
		myInput.style.width = "80%";
		myInput.style.height = "30%";
		issueId = issueId + String.fromCharCode(keyCode);
		myInput.textContent = issueId;
	}
	if(e.keyCode==8){
		issueId = "";
		myInput.style.width = "0%";
		myInput.style.height = "0%";
		myInput.textContent = issueId;
	}
	if (issueId.length == 4) {
		//alert(issueId);
		var myUrl = "https://fantasyflightgames.atlassian.net/browse/LRIT-" + issueId;
		issueId = "";
		myInput.style.width = "0%";
		myInput.style.height = "0%";
		//myInput.textContent = issueId;
		window.open(myUrl,"_self");
	}
});
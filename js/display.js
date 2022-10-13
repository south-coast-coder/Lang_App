function display(number)
{console.log("test")
if(number==1){
document.getElementById("about").innerHTML = " <h1>HTML/CSS </h1>At the moment I am brushing up on my html and css skills so I understand how modern websites are built at least on a basic level"
}
else if (number==2){
	document.getElementById("about").innerHTML = "<h1>Github </h1>I have created a repository on github and am uploading changes to it from my computer in order to learn the key commands and the general workflow of version control"
}
else if (number==3){
	document.getElementById("about").innerHTML = "<h1> Javascript </h1> I am learning Javascript by adding scripts to this page, I have linked to a JS file that allows the content of this box to be updated when the user clicks on one of the images above."
}
else{
	console.log("neither")
}
}
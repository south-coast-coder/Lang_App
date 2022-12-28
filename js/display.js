function display(number)
{console.log("test")
if(number==1){
	setTimeout(function(){
document.getElementById("about").innerHTML = " <h1>HTML/CSS </h1>At the moment I am brushing up on my html and css skills so I understand how modern websites are built at least on a basic level"
},0)
}
else if (number==2){
	setTimeout(function(){
	document.getElementById("about").innerHTML = "<h1>Github </h1>I have created a repository on github and am uploading changes to it from my computer in order to learn the key commands and the general workflow of version control"
}0)
}
else if (number==3){
	document.getElementById("about").innerHTML = "<h1> Javascript </h1> I am learning Javascript by adding scripts to this page, I have linked to a JS file that allows the content of this box to be updated when the user clicks on one of the images above."
}
else if (number ==4){
	document.getElementById("about").innerHTML = "<h1>Chess</h1> I am improving my Javascript files by building a chess game which I will host on Github Pages... <br> <a href='https://github.com/south-coast-coder/chess-game-2'>Repository Here</a>   <a href='https://south-coast-coder.github.io/chess-game-2/'>Link here</a>"
}
else{
	console.log("neither")
}
}
function transform(number){
	if(number ==1){
		console.log("One")
		
		document.getElementById("blog-cont").innerHTML = `<img src=\"forward.png\"style=\"width:2vw;height:2vw;margin-top:7vw;\" class=\"rotateimg180\"></div>
    <div class =\"blog-box\"><img src=\"python.jpeg\" class=\"placeholder\" onclick=\"display(4)\">></div>
    <div class =\"blog-box\"> <img src=\"images/git-session.png\" class=\"placeholder\" onclick=\"display(2)\"> <div id=\"blog1title\">Github</div></div>
   <div class =\"blog-box\"><img src=\"js.png\" class=\"placeholder\" onclick=\"display(3)\"></div>
    <img src=\"forward.png\" style=\"width:2vw;height:2vw;margin-top:7vw;\" onclick=\"transform(2)\"></div>`
}
else if (number ==2){ 
	console.log("TWO")
	document.getElementById("blog-cont").innerHTML =`<img src=\"forward.png\"style=\"width:2vw;height:2vw;margin-top:7vw;\" class=\"rotateimg180\"onclick=\"transform(1)\"></div>
    <div class =\"blog-box\"><img src=\"html.jpeg\" class=\"placeholder\" onclick=\"display(1)\">></div>
    <div class =\"blog-box\"> <img src=\"images/git-session.png\" class=\"placeholder\" onclick=\"display(2)\"> <div id=\"blog1title\">Github</div></div>
   <div class =\"blog-box\"><img src=\"js.png\" class=\"placeholder\" onclick=\"display(3)\"></div>
    <img src=\"forward.png\" style=\"width:2vw;height:2vw;margin-top:7vw;>\"</div>`
}
         
}
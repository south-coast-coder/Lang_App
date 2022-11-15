function move2(square){
	var current=localStorage.getItem('currentPiece');
	var lastSquare=localStorage.getItem('currentSquare');
	var turn = localStorage.getItem("turn")
	var targetSquare=(square)
	alert(current, lastSquare, turn, targetSquare)
}
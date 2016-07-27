// window.onload = function() {
// 	$(document).on('click', changePhoto);
// 	image.click(changePhoto);
// }

// function changePhoto(newurl) {
// 	var image = $(".profile").children()[0];
// 	image.src = newurl;
// }

function myFunction() {
	document.getElementById("myDropDown").classList.toggle("show");
}

window.onload = function() {
	$('.dropdown').on('click', resetDisplay);
}

function resetDisplay(event){
	$(".allProjects").hide();
	var dropItem = event.target.innerHTML;
	if(dropItem == "Arduino") {
		$("#Project1").show();
	}
	if(dropItem == "Runner Game") {
		$("#Project2").show();
	}
	if(dropItem == "Scratch") {
		$("#Project3").show();
	}
}

// function resetDisplay(event){
// 	$(".myHobbies").hide();
// 	var dropItem = event.target.innerHTML;
// 	if(dropItem == "Dance") {
// 		$("#Project1").show();
// 	}
// 	if(dropItem == "Music") {
// 		$("#Project2").show();
// }
// list.each(function) performs function for each item on the list
// document.addEventListener(load) = function() {
// 	var div = document.getElementByClassName('profile')[0];
// 	document.addEventListener('click', changePhoto);
// }

// function changePhoto(newurl) {
// 	document.getElementByClassName('profile')[0].children[0].src = newurl;
// }

//make pictures bigger by hovering over it
// $("div").hover(function() {
// 	this.animate({
// 		left: '250px',
// 		opacity: '0.5',
// 		height: '150px',
// 		width: '150px',
// 	})
// }
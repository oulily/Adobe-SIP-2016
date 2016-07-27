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

window.onload= function() {
	$(".allProjects").hide();
	var dropItem = event.target.innerHTML;
	if(dropItem == "Projects") {
		$("#projects").show();
	}
	if(dropItem == "Hobbies") {
		$("#hobbies").show();
	}
	if(dropItem == "Fun w/Fam") {
		$("#funfam").show();
	}
}
// document.addEventListener(load) = function() {
// 	var div = document.getElementByClassName('profile')[0];
// 	document.addEventListener('click', changePhoto);
// }

// function changePhoto(newurl) {
// 	document.getElementByClassName('profile')[0].children[0].src = newurl;
// }

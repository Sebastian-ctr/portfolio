//nav bar
function openNav() {
    document.getElementById("mySidenav").style.width = "100%";    
  }//250px
  
function closeNav(){
    document.getElementById("mySidenav").style.width = "0";
  }



window.onload = function() {



/* home page slide show*/
var myIndex = 0;
carousel();

function carousel(){
  var i;
  var x = document.getElementsByClassName("image-home");
  for (i = 0; i < x.length; i++){
    x[i].style.display = "none";
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}
  x[myIndex-1].style.display = "block";
  setTimeout(carousel,5000);
}
/* tittle for photo on home page*/

var myIndexTittle = 0;
carouselTittle();

function carouselTittle(){
  var i;
  var z = document.getElementsByClassName("image-home-tittle");
  for (i = 0 ; i < z.length; i++){
    z[i].style.display = "none";
  }

  myIndexTittle++;
  if (myIndexTittle > z.length){myIndexTittle = 1}
  z[myIndexTittle-1].style.display = "block";
  setTimeout(carouselTittle, 5000);
}

}



//lightbox for album detail
//open modal

function openModal(){
  document.getElementById("myModal").style.display = "block";
}

//Close the Modal
function closeModal(){
  document.getElementById("myModal").style.display = "none";
}

//next/previous controls
function plusSlides(n){
  showSlides(slideIndex += n);
}

function currentSlide(n){
  showSlides(slideIndex = n);
}


//showSlides for album detail
function showSlides(n){
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if(n > slides.length){slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i <slides.length; i++){
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}


var slideIndex = 0;
showSlides(slideIndex);







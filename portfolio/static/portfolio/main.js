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
  /* tittle for photo*/

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


//modal galeryy
var modal = document.getElementById("myModal");

//var img = document.querySelectorAll(".album-img");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

Array.from(document.querySelectorAll(".album-img")).forEach(item =>{
  item.addEventListener("click", event =>{
  modal.style.display = "block";
  modalImg.src = event.target.src;
  captionText.innerHTML = event.target.alt;
  console.log('works');
  }
  );
})

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}
//end window onload function
}
//slideshow for album detail
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n){
  console.log('plusSlides');
  showSlides(slideIndex += n);
}

function currentSlide(n){
  console.log('działa, id: ' + n);
  showSlides(slideIndex = n)
}

function showSlides(n){
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length){slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for ( i =0; i < slides.length; i++){
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}
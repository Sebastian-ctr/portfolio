//nav bar
function openNav() {
    document.getElementById("mySidenav").style.width = "100%";
  }//250px
  
function closeNav(){
    document.getElementById("mySidenav").style.width = "0";
  }

function next(){
    document.getElementById("home-img").src="static/portfolio/flower2.jpg";
}


//modal galeryy
window.onload = function() {
var modal = document.getElementById("myModal");

//var img = document.querySelectorAll(".album-img");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
/*img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
  console.log('works');
}*/
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
}
//slideshow for album detail
var slideIndex = 0;
showSlides(slideIndex);

function plusSlides(n){
  showSlides(slideIndex += n);
}

function currentSlide(n){
  console.log(n);
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
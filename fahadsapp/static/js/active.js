// $(document).on('click','.nav-item',function(){
//     $(this).addClass('active').siblings().removeClass('active')
// })

//
const sections = document.querySelectorAll("section");
const navLi = document.querySelectorAll(".header_area .main-menu .hmm #navbarNav .ul .nav-item ");
const a = document.querySelectorAll(".header_area .main-menu .hmm #navbarNav .ul .nav-item a");
window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (pageYOffset >= sectionTop - sectionHeight / 2) {
      current = section.getAttribute("id");
    }
  });
  
navLi.forEach((li)=>{
  if(li.dataset.name==current){
    console.log(li.dataset.name)
    li.classList.add('active')
  }
  else{
    li.classList.remove('active')
  }
})
});
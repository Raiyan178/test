
let header = document.getElementById('header')
window.addEventListener('scroll',function(){
    header.classList.toggle('sticky-top', window.scrollY>0)
})


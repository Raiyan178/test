$(document).ready(function(){
    $('.portfolio-item').isotope({
        itemSelector:'.item',
        layoutMode:'fitRows'
    });
    $('.navbar-nav li').click(function(){
        $('.navbar-nav li').removeClass('activate');
        $(this).addClass('activate');

        let selector =$(this).attr('data-filter');
        $('.portfolio-item').isotope({
            filter:selector
        });
        return false
    });
})
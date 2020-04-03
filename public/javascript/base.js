$(document).keyup(function(event) {
    console.log(event.which);
    if (event.which === 27) {
        window.location.replace("main_menu");
    }
});
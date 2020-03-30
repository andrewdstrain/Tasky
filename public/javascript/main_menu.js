$( function() {
    $(".menu-item").on("mousedown", function() {
        $(this).css("border-style", "inset");
    });

    $(".menu-item").on("mouseup", function() {
        $(this).css("border-style", "outset");
        window.location.assign("/" + $(this).attr("id"));
    });
});
$(function() {
    $(".menu-item").on("mousedown", function() {
        $(this).css("border-style", "inset");
    });

    $(".menu-item").on("mouseup", function() {
        $(this).css("border-style", "outset");
        window.location.assign($(this).attr("id"));
    });
});

$(document).keyup(function(event) {
    if (event.which === 67) {
        window.location.replace("add_task");
    } else if (event.which === 82) {
        window.location.replace("list_tasks");
    } else if (event.which === 85) {
        window.location.replace("complete_task");
    } else if (event.which === 68) {
        window.location.replace("remove_task");
    }
});
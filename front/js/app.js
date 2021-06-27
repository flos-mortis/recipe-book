let header = document.querySelector("#header");
let main_content = document.querySelector("#main-content");
let main_content_height = main_content.clientHeight;
let scroll_position = window.scrollY;

document.addEventListener("scroll", function() {
    scroll_position = window.scrollY;

    if(scroll_position > 88.88){
        header.classList.add("fixed");
    }
    else {
        header.classList.remove("fixed")
    }
}, false);

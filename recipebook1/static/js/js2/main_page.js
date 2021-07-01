function time_hover(value, color){
    let img = value.querySelector(".time_item_img");

    if(color === "black"){
        img.setAttribute("src", "../../static/images/alarm.png");
    }
    else {
        img.setAttribute("src", "../../static/images/main_alarm.png");
    }
    console.log(img);
}
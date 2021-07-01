function time_hover(value, color){
    let img = value.querySelector(".time_item_img");

    if(color=="black"){
        img.setAttribute("src", "../../images/alarm.png");
    }
    else {
        img.setAttribute("src", "../../images/main_alarm.png");
    }
    console.log(img);
}
function eventForm(value) {
  var gcd = function(a, b) {
    if (b < 0.0000001) return a;

    return gcd(b, Math.floor(a % b));
  };

// изменяю склонение слова "порция"
  word_after_number = document.querySelectorAll(".input-number-text")[1].querySelector("h4")

  if(value == 1) {
    word_after_number.innerHTML = "порцию"
  }
  else if(value > 1 && value < 5) {
    word_after_number.innerHTML = "порции"
  }
  else {
    word_after_number.innerHTML = "порций"
  }

// изменяю значения в таблице ингредиентов
  table_values = document.querySelectorAll(".ingredients_table_td_value")

  for(let item = 0; item < table_values.length; item ++){
    var fraction = Number(table_values[item].getAttribute("initial_value")) * value

    var len = fraction.toString().length - 2;

    var denominator = Math.pow(10, len);
    var numerator = fraction * denominator;

    var divisor = gcd(numerator, denominator);

    numerator /= divisor;
    denominator /= divisor;

    numerator = Math.floor(numerator);
    denominator = Math.floor(denominator);

    let result = Math.floor(numerator) + '/' + Math.floor(denominator);
    if(denominator == 1) {
      result = numerator;
    }
    else {
      if(numerator == denominator) {
        result = 1;
      }
      else{
        if(numerator > denominator) {
          let full_piece = Math.floor(numerator/denominator);
          numerator = numerator - denominator * full_piece;
          result = full_piece + "&nbsp" + numerator + "/" + denominator;
        }
      }
    }

    table_values[item].innerHTML = result;
  }
}

eventForm(1);

let table_height = document.querySelector(".ingredients_table").clientHeight;

let video_element =  document.querySelector(".video");

video_element.style.height = String(table_height) + "px";
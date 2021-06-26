function eventForm(value) {

// изменяю склонение слова "порция"
  word_after_number = document.querySelectorAll(".input-number-text")[1].querySelector("h4")
  console.log(word_after_number)
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
    table_values[item].innerHTML = Number(table_values[item].getAttribute("initial_value")) * value
    console.log(table_values[item].innerHTML)
  }
}
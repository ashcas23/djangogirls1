function ChangeColorofPostTitles() { //defining a (python) function
  let elements_posttitles = document.getElementsByClassName("posttitle");

  for (element of elements_posttitles){
    let colors = ["red", "green", "purple", "yellow", "orange"]
    let randomColor = colors[Math.floor(Math.random() * colors.length)]
    element.style["color"] = randomColor;
    element.style["border"] = "1px solid blue";

  }
}

let ChangeColorofTitles = document.getElementById("ChangeColorofTitles");
ChangeColorofTitles.addEventListener("click", ChangeColorofPostTitles); //if button is clicked the function gets called

function changeTitleColor() {
  let element = document.getElementById("titlelink");
  let colors = ["red", "green", "purple", "yellow", "orange"]
  let randomColor = colors[Math.floor(Math.random() * colors.length)]
  element.style["color"] = randomColor;
  element.style["border"] = "1px solid blue"
}

let ChangeColorofMainTitle = document.getElementById("ChangeColorofMainTitle");
ChangeColorofMainTitle.addEventListener("click", changeTitleColor);

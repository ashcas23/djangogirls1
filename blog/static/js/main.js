function ChangeColorofPostTitles() { //defining a (JavaScript) function
  let elements_posttitles = document.getElementsByClassName("posttitle");

  for (element of elements_posttitles){ //the loop serves as a random color generator each time the button on the blog is pressed
    let colors = ["red", "green", "purple", "yellow", "orange"]
    let randomColor = colors[Math.floor(Math.random() * colors.length)]
    element.style["color"] = randomColor;
    element.style["border"] = "1px solid blue";

  }
}

let ChangeColorofTitlesButton = document.getElementById("ChangeColorofTitlesButton");
ChangeColorofTitlesButton.addEventListener("click", ChangeColorofPostTitles); //if button is clicked the function gets called

function changeTitleColor() {
  let element = document.getElementById("titlelink");
  let colors = ["red", "green", "purple", "yellow", "orange"]
  let randomColor = colors[Math.floor(Math.random() * colors.length)]
  element.style["color"] = randomColor;
  element.style["border"] = "1px solid blue"
}

let ChangeColorofMainTitleButton = document.getElementById("ChangeColorofMainTitleButton");
ChangeColorofMainTitleButton.addEventListener("click", changeTitleColor);

let ScrollToTopButton = document.getElementById("ScrollToTopButton");

function ScrollToTopFunction() {
  let title = document.getElementById("titlelink");
  title.scrollIntoView({ behavior:"smooth", block: "center"});
}
ScrollToTopButton.addEventListener("click", ScrollToTopFunction);

function ScrollToBottomFunction() {
  let ScrollToTopButton = document.getElementById("ScrollToTopButton"); //we input the code to find the ScrollToTopButton when pressing the ScrollToBottomFunction in order for the page to go to where the ScrollToTopButton is located
  ScrollToTopButton.scrollIntoView({ behavior:"smooth", block: "center"}); //make sure to change name of the titles
}
ScrollToBottomButton.addEventListener("click", ScrollToBottomFunction);

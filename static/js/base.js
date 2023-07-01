"use strict";
var menuIsOpened = false;
var titleOfPage = document.getElementById("titleOfPage").innerText;
function clickingMenu() {
  let menu = document.getElementById("wrapperTotalSecondMenu").style;
  let menuBtn = document.getElementById("menuIconBtn");
  if (!menuIsOpened) {
    if (
      titleOfPage == "\n      SignUp\n    " ||
      titleOfPage == "\n      Login\n    "
    ) {
      menuBtn.setAttribute("src", "../../static/Image/CrossIcon.svg");
    } else {
      menuBtn.setAttribute("src", "../static/Image/CrossIcon.svg");
    }

    menuBtn.setAttribute("class", "crossIcon");
    menu.right = "0";
    menu.transition = "1s";
    menuIsOpened = true;
  } else {
    if (
      titleOfPage == "\n      SignUp\n    " ||
      titleOfPage == "\n      Login\n    "
    ) {
      menuBtn.setAttribute("src", "../../static/Image/MenuIcon.svg");
    } else {
      menuBtn.setAttribute("src", "../static/Image/MenuIcon.svg");
    }
    menuBtn.removeAttribute("class", "crossIcon");
    menu.right = "-41%";
    menu.transition = "1s";
    menuIsOpened = false;
  }
}
function changingScreenDisplay() {
  let widthOfScreen = screen.width;
  let menu = document.getElementById("wrapperTotalSecondMenu").style;
  let menuBtn = document.getElementById("menuIconBtn");
  if (widthOfScreen > 1070) {
    if (
      titleOfPage == "\n      SignUp\n    " ||
      titleOfPage == "\n      Login\n    "
    ) {
      menuBtn.setAttribute("src", "../../static/Image/MenuIcon.svg");
    } else {
      menuBtn.setAttribute("src", "../static/Image/MenuIcon.svg");
    }
    menuBtn.removeAttribute("class", "crossIcon");
    menu.right = "-41%";
    menu.transition = "1s";
    menuIsOpened = false;
  }
}

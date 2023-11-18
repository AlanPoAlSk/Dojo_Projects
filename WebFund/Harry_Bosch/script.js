// BOOK SECTION +++++++++++++++++++++++++++++++++++++++

function openBooks() {
    let container = document.getElementById("contain");
    let window = document.getElementById("popup1");
    window.style.display = "block";
    container.style.filter = "blur(10px)";
}
function hide1() {
    let container = document.getElementById("contain");
    let window = document.getElementById("popup1");
    window.style.display = "none";
    container.style.filter = "none";
}

//  AUTHOR & CHARACTER SECTION +++++++++++++++++++++++++

function onW() {
    let wiki = document.getElementById("titus");
    wiki.style.visibility = "visible";
}
function offW() {
    let wiki = document.getElementById("titus");
    wiki.style.visibility = "hidden";
}

function onM() {
    let wiki2 = document.getElementById("michael");
    wiki2.style.visibility = "visible";
}
function offM() {
    let wiki2 = document.getElementById("michael");
    wiki2.style.visibility = "hidden";
}

// ++++++++++++++++++++++++++++++++++++++++++++++++++++++

//  MUSIC SECTION +++++++++++++++++++++++++++++++++++++++

function openMusic() {
    let musicP = document.getElementById("musicPlayer");
    musicP.style.display = "block";
}
function hideMusic() {
    let musicP = document.getElementById("musicPlayer");
    musicP.style.display = "none";
}

//  +++++++++++++++++++++++++++++++++++++++++++++++++++++

// MENU SECTION +++++++++++++++++++++++++++++++++++++++++

function openmenu() {
    let menu = document.getElementById("menupart");
    let menu2 = document.getElementById("menupart2");
    menu.style.visibility = "visible";
    menu2.style.visibility= "visible";
}
function hidemenu() {
    let menu = document.getElementById("menupart");
    let menu2 = document.getElementById("menupart2");
    menu.style.visibility = "hidden";
    menu2.style.visibility = "hidden";
}

// ++++++++++++++++++++++++++++++++++++++++++++++++++++++

//  TV SERIES SECTION +++++++++++++++++++++++++++++++++++

function openTVS() {
    let buttonTVS = document.getElementById("closingTVS")
    let part2 = document.getElementById("menupart2")
    let container = document.getElementById("contain");
    let tvs = document.getElementById("originalimg");
    let tvs2 = document.getElementById("spinoffimg");
    tvs.style.visibility = "visible";
    tvs2.style.visibility = "visible";
    container.style.filter = "blur(10px)";
    part2.style.filter= "blur(10px)";
    buttonTVS.style.visibility= "visible";
}

function closeTVS() {
    let buttonTVS = document.getElementById("closingTVS")
    let part2 = document.getElementById("menupart2")
    let container = document.getElementById("contain");
    let tvs = document.getElementById("originalimg");
    let tvs2 = document.getElementById("spinoffimg");
    tvs.style.visibility = "hidden";
    tvs2.style.visibility = "hidden";
    container.style.filter = "none";
    part2.style.filter= "none";
    buttonTVS.style.visibility= "hidden";
}

function openSeasonOr() {
    let listOr = document.getElementById("seriesOr")
    listOr.style.visibility= "visible"
}

function closeSeasonOr() {
    let listOr = document. getElementById("seriesOr")
    listOr.style.visibility= "hidden";
}

function openSeasonLe() {
    let listLe = document.getElementById("seriesLe")
    listLe.style.visibility= "visible"
}

function closeSeasonLe() {
    let listLe = document. getElementById("seriesLe")
    listLe.style.visibility= "hidden";
}


// function on() {
//     let image = document.getElementById("jazz");
//     image.style.display = "block";
// }
// function off() {
//     let image = document.getElementById("jazz");
//     image.style.display = "none";
// }


let slides = document.querySelectorAll(".slide");

function slideS() {

    let current = document.querySelector(".active");

    current.classList.remove("active");

    if (current.nextElementSibling) {
        current.nextElementSibling.classList.add("active")
    }
    else {
        slides[0].classList.add("active");
    }
    setTimeout("slideS()", 8000)
}

window.onload= slideS



// function buttonShowing() {
//     let buttonShow = document.getElementById("loadButton")
//     buttonShow.style.visibility = "none"
//     setTimeout((buttonShowing,delay) => {
//         console.log("Delayed for 10 second.");
//     }, 10000);
// }


function removeLoadingPage() {
    let removeLpage = document.getElementById("leader1");
    removeLpage.style.height = 0
}

var button = document.getElementById('show_button')
button.addEventListener('click',hideshow,false);

function hideshow() {
    var buttontoRemove = document.getElementById("loadButton")
    buttontoRemove.style.visibility = 'hidden'
    }   
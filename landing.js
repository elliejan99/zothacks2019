function displayHidden(){
  var x = document.getElementById("hidden");
  var bg = document.getElementById("bg");
  var gs = document.getElementById("getStarted");
  var logo = document.getElementById("logo");
  x.style.display = "block";
  bg.style.opacity = "0.5";
  gs.style.display = "none";
  logo.style.display = "none";
}

function hideHidden(){
  var x = document.getElementById("hidden");
  var bg = document.getElementById("bg");
  var gs = document.getElementById("getStarted");
  var logo = document.getElementById("logo");
  if (x.style.display == "block"){
    document.getElementById("hidden").style.display = "none";
  }
  bg.style.opacity = "1";
  gs.style.display = "block";
  logo.style.display = "block";
}

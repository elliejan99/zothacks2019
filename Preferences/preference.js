function nameNext(){
  var x = document.getElementById("name");
  var y = document.getElementById("major");
  x.style.display = "none";
  y.style.display = "block";
}

function majorBefore(){
  var x = document.getElementById("name");
  var y = document.getElementById("major");
  x.style.display = "block";
  y.style.display = "none";
}

function majorNext(){
  var x = document.getElementById("major");
  var y = document.getElementById("year");
  x.style.display = "none";
  y.style.display = "block";
}

function yearBefore(){
  var x = document.getElementById("major");
  var y = document.getElementById("year");
  x.style.display = "block";
  y.style.display = "none";
}

function yearNext(){
  var x = document.getElementById("year");
  var y = document.getElementById("housing");
  x.style.display = "none";
  y.style.display = "block";
}

function housingBefore(){
  var x = document.getElementById("year");
  var y = document.getElementById("housing");
  x.style.display = "block";
  y.style.display = "none";
}

function housingNext(){
  var x = document.getElementById("housing");
  var y = document.getElementById("political");
  x.style.display = "none";
  y.style.display = "block";
}

function politicalBefore(){
  var x = document.getElementById("housing");
  var y = document.getElementById("political");
  x.style.display = "block";
  y.style.display = "none";
}

function politicalNext(){
  var x = document.getElementById("political");
  var y = document.getElementById("interest");
  x.style.display = "none";
  y.style.display = "block";
}

function interestBefore(){
  var x = document.getElementById("political");
  var y = document.getElementById("interest");
  x.style.display = "block";
  y.style.display = "none";
}

function interestNext(){
  var x = document.getElementById("interest");
  var y = document.getElementById("value");
  x.style.display = "none";
  y.style.display = "block";
}

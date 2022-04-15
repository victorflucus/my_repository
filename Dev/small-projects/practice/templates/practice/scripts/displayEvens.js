//Two functions are neccessary:
// A function that handles reseting the form after user executes script.
// A function that handles determining the even numbers
// Inputs: Starting number, ending number, increment
// Outputs: all the even numbers between the start and end value.


//Getting user entries
var evenNumbers = document.forms["evenNumbers"];
var strt = document.getElementById("strt");
var end = document.getElementById("end");
var incr = document.getElementById("incr");
var results = document.getElementById("results");
var submitButton = document.getElementById("submitButton");


function validate() {

// Validation logic
    evenNumbers.className = "needs-validation";

    if (!evenNumbers.checkValidity()) {
        evenNumbers.className = "was-validated";
        return false;
    }
// Even numbers function logic:

  // initializing working variables
    var initial = parseInt(strt.value, 10);
    var fin = parseInt(end.value, 10);
    var step = parseInt(incr.value, 10);
    var set = new Array();
    var evens = new Array();

  // Defining working set
    set.length = Math.floor(((fin-initial)/step) - 1);
    for (var ind = 0; ind < set.length; ind++) {
      set[ind] = (initial + step);
      initial = set[ind];
    }
  // Defining evens within the working set
    for (var i = 0; i < set.length; i++){
      if ((set[i] % 2) == 0) {
        evens.push(set[i]);
      }
    }


}

//if true, we're tracking the mouse.
var tracking = false;
// Grab  DOM references to be used in all functions.
var mouseX = document.getElementById("mouseX");
var mouseY = document.getElementById("mouseY");
var onButton = document.getElementById("btnToggleOn");
var offButton = document.getElementById("btnToggleOff");

function toggle() {
  // 'this' here is the HTML element that triggered the event.
  // When we're done, it will be button toggle

  // classList is an array-lile collection of CSS class names:
  // (https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)
  //It allows us to treat class names individually
  // instead of setting all classes at once:
  // element.className = "btn btn-default btn-lrg"

  if (tracking) { // mouse tracking is off
    offButton.classList.remove("btn-danger");
    offButton.classList.add("btn-basic");
    offButton.innerText = "Mouse Tracking Off";

    onButton.classList.remove("btn-basic");
    onButton.classList.add("btn-success");
    onButton.innerText = "Start mouse tracking";

    mouseX.innerText = "Untracked" ;
    mouseY.innerText = "Untracked";

  } else { // mouse tracking is on
    onButton.classList.remove("btn-success");
    onButton.classList.add("btn-basic");
    onButton.innerText = "Mouse Tracking On";

    offButton.classList.remove("btn-basic");
    offButton.classList.add("btn-danger");
    offButton.innerText = "Stop Mouse Tracking";

  }
  tracking = !tracking;
}

function updateMousePosition(evt){
  //If tracking is enabled, update this view.
  if (tracking) {
    // 'evt' is a JavaScript event object.
    // It contains different properties depending on the type of event.:
    // click, submit, mouseover, even media platback
    // (https://developer.mozilla.org/en-US/docs/Web/Events).
    // Our mouse's position in X and Y coordinates is clientX, clientY.
    mouseX.innerText = evt.clientX;
    mouseY.innerText = evt.clientY;
  }
}

// Note that the functions toggle and updateMousePosition are not executed.
// Execution would be toggle() and updateMousePosition(event).
// Instead, a reference to the function (its name) is attached to the DOM.
document.getElementById("btnToggleOn").addEventListener("click", toggle);
document.getElementById("btnToggleOff").addEventListener("click", toggle);
document.addEventListener("mousemove", updateMousePosition);

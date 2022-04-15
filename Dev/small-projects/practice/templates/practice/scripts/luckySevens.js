// Lucky Sevens

// Function:
//  The program asks the user how many dollars they have to bet.
//  If the starting bet is less than or equal to 0, display an error message.
//  When the user clicks the Play button, the program then rolls the dice
//  repeatedly until all the money is gone.

// Variables:
//  Statring bet.
//  how many rolls were taken before the money ran out.
//  the maximum amount of money held by the player.
//  how many rolls were taken at the point when the user held the most money.

// Output:
//  Starting Bet: with the value of the original bet
//  Total Rolls Before Going Broke: with the number of rolls the program completed before the bet value reached 0 (or less).
//  Highest Amount Won: with the maximum amount of money the pot held during the game
//  Roll Count at Highest Amount Won: with the roll count that corresponds to the highest amount won

// Get User Entries and define Variables:
var luckySevens = document.forms["luckySevens"];
var bet = document.getElementById('bet')
var results = document.getElementById("results");
var playButton = document.getElementById("playButton");

// Functions:

// Dice Rolling
function rollDice(numSides) {
    return Math.floor(Math.random() * numSides) + 1;

    // Generates a random integer between 0 and 1
    // Multiplying that integer by 6 equates to the output being between 0 and (numSides-1)
    // rounding that integer down gives you whole numbers between 0 and (numSides-1)
    //   (round down instead of up because rounding up yeilds values that cannot be less than 1)
    // Add 1 to that number in order to change the range of the out put to 1<x<numSides
}

// Form validation and game logic
function validate() {
  // Validation Logic
  luckySevens.className = "needs-validation";

  if (!luckySevens.checkValidity()) {
      luckySevens.className = "was-validated";
      return false;
  }

  // Game Logic
    // Initializing Variables
    var startingBet = parseInt(bet.value,10);
    var gameMoney = startingBet;
    var currentSum = 0;
    var lastNumberOfRolls = 0;
    var highestWon = 0;
    var bestRollCount = 0;
    var tracker = new Array();

    while (gameMoney > 0){
      // Keeping Track of users money
      tracker[lastNumberOfRolls] = gameMoney
      // Increment roll counter
      lastNumberOfRolls++;
      // Roll the dice
      currentSum = rollDice(6) + rollDice(6);
      // adjust game money according to sum
      if (currentSum === 7){
        gameMoney = gameMoney + 4;
      } else {
        gameMoney = gameMoney - 1;
      }
      // Max money won
      if (highestWon < gameMoney){
        highestWon = gameMoney;
      }
    }
        // Determining  bestRollCount
        var x = Math.max(...tracker);
        bestRollCount = tracker.findIndex(tracker => tracker === x)

// Return Results to user:
document.getElementById("startingBet").innerText = startingBet;
document.getElementById("lastNumberOfRolls").innerText = lastNumberOfRolls;
document.getElementById("highestWon").innerText = highestWon;
document.getElementById("bestRollCount").innerText = bestRollCount;

//Styling results
    results.style.display = "block";

    // We always return false so that the form doesn't submit.
    // Submission causes the page to reload.
    return false;
}

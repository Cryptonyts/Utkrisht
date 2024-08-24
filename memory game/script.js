const cards = document.querySelectorAll(".card");
const startButton = document.getElementById("startButton");
const streakElement = document.getElementById("streak"); // Element to display current streak
const highestStreakElement = document.getElementById("highestStreak"); // Element to display highest streak

let matchedCard = 0;
let cardOne, cardTwo;
let disableDeck = true; // Initially disable the deck until the game starts
let lastMatchCorrect = false; // Track if the last match was correct
let streak = 0; // Initialize streak counter
let highestStreak = localStorage.getItem('highestStreak') || 0; // Retrieve highest streak from localStorage

function flipCard(e) {
    let clickedCard = e.target;
    if (clickedCard !== cardOne && !disableDeck) {
        clickedCard.classList.add("flip");
        if (!cardOne) {
            return cardOne = clickedCard;
        }
        cardTwo = clickedCard;
        disableDeck = true;
        let cardOneImg = cardOne.querySelector("img").src,
            cardTwoImg = cardTwo.querySelector("img").src;
        matchCards(cardOneImg, cardTwoImg);
    }
}

function matchCards(img1, img2) {
    if (img1 === img2) {
        matchedCard++;
        if (matchedCard == 8) {
            setTimeout(() => {
                return shuffleCard();
            }, 1000);
        }
        cardOne.removeEventListener("click", flipCard);
        cardTwo.removeEventListener("click", flipCard);
        cardOne = cardTwo = "";

        // Increment streak if the previous match was correct
        if (lastMatchCorrect) {
            streak++;
        } else {
            streak = 1; // Start a new streak
        }
        lastMatchCorrect = true; // Current match is correct

        // Update streak display
        streakElement.textContent = `Streak: ${streak}`;

        // Update highest streak
        if (streak > highestStreak) {
            highestStreak = streak;
            localStorage.setItem('highestStreak', highestStreak); // Save to localStorage
            highestStreakElement.textContent = `Highest Streak: ${highestStreak}`;
        }

        return disableDeck = false;
    } else {
        lastMatchCorrect = false; // Current match is incorrect
        streak = 0; // Reset streak to 0
        streakElement.textContent = `Streak: ${streak}`; // Update streak display

        setTimeout(() => {
            cardOne.classList.add("shake");
            cardTwo.classList.add("shake");
        }, 400);

        setTimeout(() => {
            cardOne.classList.remove("shake", "flip");
            cardTwo.classList.remove("shake", "flip");
            cardOne = cardTwo = "";
            disableDeck = false;
        }, 1200);
    }
}

function shuffleCard() {
    matchedCard = 0;
    cardOne = cardTwo = "";
    disableDeck = false; // Enable the deck after shuffling
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8];
    arr.sort(() => Math.random() > 0.5 ? 1 : -1);
    cards.forEach((card, index) => {
        card.classList.remove("flip");
        let imgTag = card.querySelector("img");
        imgTag.src = `img${arr[index]}.png`;
        card.addEventListener("click", flipCard);
    });
}

startButton.addEventListener("click", () => {
    // Tilt all tiles for 4 seconds and then start the game
    cards.forEach(card => {
        card.classList.add("flip");
    });

    setTimeout(() => {
        cards.forEach(card => {
            card.classList.remove("flip");
        });
        // Do not shuffle the cards again here
        disableDeck = false; // Enable the deck after the start button is pressed
    }, 4000);
});

// Initial setup to shuffle and setup the cards
shuffleCard();

// Update highest streak display initially
highestStreakElement.textContent = `Highest Streak: ${highestStreak}`;

cards.forEach(card => {
    card.addEventListener("click", flipCard);
});

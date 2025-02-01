// Sample data (can be replaced with an API call)
const profiles = [
    {
      id: 1,
      name: "Startup A",
      description: "Revolutionizing AI in healthcare.",
      image: "assets/startup1.jpg",
    },
    {
      id: 2,
      name: "Investor X",
      description: "Focuses on early-stage tech startups.",
      image: "assets/investor1.jpg",
    },
    // Add more profiles here
  ];
  
  let currentIndex = 0;
  const cardContainer = document.getElementById("card-container");
  
  // Function to render a card
  function renderCard(profile) {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <img src="${profile.image}" alt="${profile.name}">
      <h2>${profile.name}</h2>
      <p>${profile.description}</p>
    `;
    cardContainer.appendChild(card);
  }
  
  // Function to load next card
  function loadNextCard() {
    if (currentIndex < profiles.length) {
      renderCard(profiles[currentIndex]);
      currentIndex++;
    } else {
      cardContainer.innerHTML = "<p>No more profiles to show.</p>";
    }
  }
  
  // Swipe Left (Reject)
  document.getElementById("swipe-left").addEventListener("click", () => {
    const card = document.querySelector(".card");
    if (card) {
      card.style.transform = "translateX(-100%) rotate(-30deg)";
      setTimeout(() => {
        card.remove();
        loadNextCard();
      }, 300);
    }
  });
  
  // Swipe Right (Accept)
  document.getElementById("swipe-right").addEventListener("click", () => {
    const card = document.querySelector(".card");
    if (card) {
      card.style.transform = "translateX(100%) rotate(30deg)";
      setTimeout(() => {
        card.remove();
        loadNextCard();
      }, 300);
    }
  });
  
  // Load the first card
  loadNextCard();
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
  
  // VC Profile Form Submission
  document.getElementById("vc-profile-form")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const vcProfile = Object.fromEntries(formData.entries());
    console.log("VC Profile:", vcProfile);
    alert("VC Profile Saved!");
    e.target.reset();
  });

  // Startup Profile Form Submission
  document.getElementById("startup-profile-form")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const startupProfile = Object.fromEntries(formData.entries());
    console.log("Startup Profile:", startupProfile);
    alert("Startup Profile Saved!");
    e.target.reset();
  });

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  // Login Form Submission
document.getElementById("login-form")?.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  // Basic validation
  if (!email || !password) {
    alert("Please fill in all fields.");
    return;
  }

  // Simulate login (replace with actual API call)
  console.log("Login Data:", { email, password });
  alert("Login successful! Redirecting to dashboard...");

  // Redirect to dashboard or home page
  window.location.href = "index.html";
});

// Signup Form Submission
document.getElementById("signup-form")?.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const role = document.getElementById("role").value;

  // Basic validation
  if (!name || !email || !password || !role) {
    alert("Please fill in all fields.");
    return;
  }

  // Simulate signup (replace with actual API call)
  console.log("Signup Data:", { name, email, password, role });
  alert("Signup successful! Redirecting to profile creation...");

  // Redirect based on role
  if (role === "vc") {
    window.location.href = "vc-profile.html";
  } else if (role === "startup") {
    window.location.href = "startup-profile.html";
  }
});

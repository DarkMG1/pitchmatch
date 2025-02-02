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
// Example: Create VC Profile
document.getElementById("vc-profile-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const token = localStorage.getItem("token");  // Get token from localStorage
  if (!token) {
    alert("You must be logged in to create a profile.");
    return;
  }

  const budget = document.getElementById("budget").value;
  const industry = document.getElementById("industry").value;
  const businessSize = document.getElementById("business-size").value;
  const equity = document.getElementById("equity").value;
  const location = document.getElementById("location").value;
  const certifications = document.getElementById("certifications").value;
  const tags = document.getElementById("tags").value;

  try {
    const response = await fetch("http://localhost:5000/profile/vc", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": token,  // Include token in headers
      },
      body: JSON.stringify({ budget, industry, business_size: businessSize, equity, location, certifications, tags }),
    });

    const data = await response.json();
    if (response.ok) {
      alert(data.message);
    } else {
      alert(data.error);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("An error occurred. Please try again.");
  }
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

// Signup Form Submission
document.getElementById("signup-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const role = document.getElementById("role").value;

  if (!name || !email || !password || !role) {
    alert("Please fill in all fields.");
    return;
  }

  try {
    const response = await fetch("http://localhost:5000/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email, password, role }),
    });

    const data = await response.json();
    if (response.ok) {
      alert(data.message);
      window.location.href = role === "vc" ? "vc-profile.html" : "startup-profile.html";
    } else {
      alert(data.error);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("An error occurred. Please try again.");
  }
});

// Login Form Submission
document.getElementById("login-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!email || !password) {
    alert("Email and password are required.");
    return;
  }

  try {
    const response = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (response.ok) {
      alert(data.message);
      localStorage.setItem("token", data.token);  // Save token to localStorage
      window.location.href = "index.html";  // Redirect to home page
    } else {
      alert(data.error);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("An error occurred. Please try again.");
  }
});

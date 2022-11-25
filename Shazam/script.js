document.querySelector(".navbar_links").addEventListener("click", function (e) {
    e.preventDefault();
  
    if (e.target.classList.contains("nav__link")) {
      const id = e.target.getAttribute("href");
      document.querySelector(id).scrollIntoView({ behavior: "smooth" });
    }
  });
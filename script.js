const tabsContainer = document.querySelector(".how_to_tab-container");
const tabs = document.querySelectorAll(".how_to_tab");
const tabsContent = document.querySelectorAll(".how_to_contents");
const nav = document.querySelector(".navbar");
const navHeight = nav.getBoundingClientRect().height;
// Tabbed component

tabsContainer.addEventListener("click", function (e) {
  const clicked = e.target.closest(".how_to_tab");

  if (!clicked) return;

  tabs.forEach((t) => t.classList.remove("how_to_tab--active"));
  tabsContent.forEach((c) => c.classList.remove("how_to_contents--active"));

  clicked.classList.add(`how_to_tab--active`);

  document
    .querySelector(`.how_to_contents--${clicked.dataset.tab}`)
    .classList.add("how_to_contents--active");
});

// Smooth scrolling

document.querySelector(".navbar_links").addEventListener("click", function (e) {
  e.preventDefault();

  if (e.target.classList.contains("nav__link")) {
    const id = e.target.getAttribute("href");
    document.querySelector(id).scrollIntoView({ behavior: "smooth" });
  }
});

// Sticky Navbar

const stickyNav = function (entries) {
  const [entry] = entries;

  if (!entry.isIntersecting) nav.classList.add("sticky");
  else nav.classList.remove("sticky");
};

const headerObserver = new IntersectionObserver(stickyNav, {
  root: null,
  threshold: 0,
  rootMargin: `-${navHeight}px`,
});

// Slider

const slider = function () {
  const slides = document.querySelectorAll(".customer_requests_ele");
  const btnLeft = document.querySelector(".customer_request_btn--left");
  const btnRight = document.querySelector(".customer_request_btn--right");
  const dotContainer = document.querySelector(".dots");

  let curSlide = 0;
  const maxSlide = slides.length - 2;

  // Functions
  const createDots = function () {
    slides.forEach(function (_, i) {
      dotContainer.insertAdjacentHTML(
        "beforeend",
        `<button class="dots__dot" data-slide="${i}"></button>`
      );
    });
  };

  const activateDot = function (slide) {
    document
      .querySelectorAll(".dots__dot")
      .forEach((dot) => dot.classList.remove("dots__dot--active"));

    document
      .querySelector(`.dots__dot[data-slide="${slide}"]`)
      .classList.add("dots__dot--active");
  };

  const goToSlide = function (slide) {
    slides.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
    );
  };

  // Next slide
  const nextSlide = function () {
    if (curSlide === maxSlide - 1) {
      curSlide = 0;
    } else {
      curSlide++;
    }

    goToSlide(curSlide);
    activateDot(curSlide);
  };

  const prevSlide = function () {
    if (curSlide === 0) {
      curSlide = maxSlide - 1;
    } else {
      curSlide--;
    }
    goToSlide(curSlide);
    activateDot(curSlide);
  };

  const init = function () {
    goToSlide(0);
    createDots();

    activateDot(0);
  };
  init();

  // Event handlers
  btnRight.addEventListener("click", nextSlide);
  btnLeft.addEventListener("click", prevSlide);

  document.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") prevSlide();
    e.key === "ArrowRight" && nextSlide();
  });

  dotContainer.addEventListener("click", function (e) {
    if (e.target.classList.contains("dots__dot")) {
      const { slide } = e.target.dataset;
      goToSlide(slide);
      activateDot(slide);
    }
  });
};
slider();

// Review Slider

const reviewSlider = function () {
  const slides = document.querySelectorAll(".review--holder");
  const btnLeft = document.querySelector(".review_btn--left");
  const btnRight = document.querySelector(".review_btn--right");
  const dotContainer = document.querySelector(".review_dots");

  let curSlide = 0;
  const maxSlide = slides.length;

  // Functions
  const createDots = function () {
    slides.forEach(function (_, i) {
      dotContainer.insertAdjacentHTML(
        "beforeend",
        `<button class="review__dots__dot" data-slide="${i}"></button>`
      );
    });
  };

  const activateDot = function (slide) {
    document
      .querySelectorAll(".review__dots__dot")
      .forEach((dot) => dot.classList.remove("dots__dot--active"));

    document
      .querySelector(`.dots__dot[data-slide="${slide}"]`)
      .classList.add("dots__dot--active");
  };

  const goToSlide = function (slide) {
    slides.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
    );
  };

  // Next slide
  const nextSlide = function () {
    if (curSlide === maxSlide) {
      curSlide = 0;
    } else {
      curSlide++;
    }

    goToSlide(curSlide);
    activateDot(curSlide);
  };

  const prevSlide = function () {
    if (curSlide === 0) {
      curSlide = maxSlide;
    } else {
      curSlide--;
    }
    goToSlide(curSlide);
    activateDot(curSlide);
  };

  const init = function () {
    goToSlide(0);
    createDots();

    activateDot(0);
  };
  init();

  // Event handlers
  btnRight.addEventListener("click", nextSlide);
  btnLeft.addEventListener("click", prevSlide);

  // document.addEventListener("keydown", function (e) {
  //   if (e.key === "ArrowLeft") prevSlide();
  //   e.key === "ArrowRight" && nextSlide();
  // });

  // dotContainer.addEventListener("click", function (e) {
  //   if (e.target.classList.contains("dots__dot")) {
  //     const { slide } = e.target.dataset;
  //     goToSlide(slide);
  //     activateDot(slide);
  //   }
  // });
};
reviewSlider();

class Slider {
  constructor() {
      this.slides = document.querySelectorAll(".slide");
      this.dots = document.querySelectorAll(".slider-dot");
      this.slideIndex = 0;
      this.intervalId = null;
      this.auto = true;
      this.delay = parseInt(document.getElementById("intervalValue").value) || 3000;
  }

  initializeSlider() {
      if (this.slides.length > 0) {
          this.showSlide();
          this.startAutoSlide();
          this.slides.forEach(slide => {
              slide.addEventListener("mouseenter", () => this.stopAutoSlide());
              slide.addEventListener("mouseleave", () => this.startAutoSlide());
          });
      }
  }

  showSlide() {
      this.slides.forEach(slide => slide.classList.remove("displaySlide"));
      this.dots.forEach(dot => dot.classList.remove("active-dot"));
      
      this.slides[this.slideIndex].classList.add("displaySlide");
      this.dots[this.slideIndex].classList.add("active-dot");
  }

  prevSlide() {
      this.stopAutoSlide();
      this.slideIndex = (this.slideIndex - 1 + this.slides.length) % this.slides.length;
      this.showSlide();
      this.startAutoSlide();
  }

  nextSlide() {
      this.stopAutoSlide();
      this.slideIndex = (this.slideIndex + 1) % this.slides.length;
      this.showSlide();
      this.startAutoSlide();
  }

  startAutoSlide() {
      if (this.auto) { 
          this.intervalId = setInterval(() => this.nextSlide(), this.delay);
      }
  }

  stopAutoSlide() {
      clearInterval(this.intervalId);
  }

  goToSlide(index) {
      this.stopAutoSlide();
      this.slideIndex = index;
      this.showSlide();
      this.startAutoSlide();
  }
}

let slider;

document.addEventListener("DOMContentLoaded", () => {
  slider = new Slider();
  slider.initializeSlider();
});
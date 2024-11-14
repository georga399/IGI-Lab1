document.addEventListener("DOMContentLoaded", () => {
  // const palmsLeft = document.querySelector('#palms_left');
  const palmsRight = document.querySelector('#palms_right');
  const cloud1 = document.querySelector('#clouds_1');
  const cloud2 = document.querySelector('#clouds_2');
  const text = document.querySelector('#text-hotel');
  const house = document.querySelector('#house-on-beach');
  palmsRight.style.left = `${window.innerWidth/2}px`;
  
  window.addEventListener('scroll',()=>{
      let value = scrollY;
      palmsRight.style.left = `${window.innerWidth/2 + value}px`;
      cloud2.style.left = `-${value*2}px`
      house.style.left = `-${value/0.7}px`
      cloud1.style.left = `${value*2}px`
      text.style.bottom = `${-value}px`;
      // house.style.height = `${window.innerHeight - value}px`
  })
});
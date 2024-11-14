const cards = document.querySelectorAll('.room-item');

cards.forEach(card => {

  card.addEventListener('mousemove', (e) => {
    // Get the card's size 
    const cardRect = card.getBoundingClientRect();
    
    // Calculate the position of the mouse relative to the card's top-left corner
    const x = e.clientX - cardRect.left; 
    const y = e.clientY - cardRect.top;  
    
    // center of the card
    const centerX = cardRect.width / 2;
    const centerY = cardRect.height / 2;
    
    // Calculate the rotation angles based on mouse position
    const rotateX = ((y - centerY) / centerY) * 30; 
    const rotateY = ((centerX - x) / centerX) * 30; 
    
    // Apply the calculated rotation to the card
    card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
  });
  
  // when the mouse leaves the card area
  card.addEventListener('mouseleave', () => {
    // Reset the card's rotation when the mouse leaves
    card.style.transform = 'rotateX(0) rotateY(0)';
  });
});

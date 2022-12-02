gsap.to('#sphere', {
    duration: 1,
    opacity: 0.5,
    repeat: -1,
    yoyo: true,
  });
  
  gsap.to('#loading', {
    duration: 1,
    opacity: 0,
    repeat: -1,
    yoyo: true,
  })
   
  setInterval(() => { 
    document.getElementById('sphere').style.backgroundPosition = `top ${Math.round(Math.random() * 8)}px left ${Math.round(Math.random() * 8)}px`;
  }, 50);
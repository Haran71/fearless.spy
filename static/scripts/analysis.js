
document.addEventListener('DOMContentLoaded',(e) => {
    text = "Fearless Spy Report";
    i = 0;


    function typeWriter(text, i, fnCallback) {
        // chekc if text isn't finished yet
        if (i < (text.length)) {
          // add next character to h1
         document.querySelector("h1").innerHTML = text.substring(0, i+1) +'<span aria-hidden="true"></span>';
    
          // wait for a while and call this function again for next character
          setTimeout(function() {
            typeWriter(text, i + 1, fnCallback)
          }, 100);
        }
        else {
            setTimeout(function() {
                $("#desc").fadeIn(3000)
                $('#ptweets').fadeIn(3000)
                $('#ntweets').fadeIn(3000)
                $('#wordcloud').fadeIn(3000)
                $('#footer').fadeIn(3000)
              }, 200);
        }
    }
    setTimeout(function(){
        $('#header').fadeIn(1000)
    },500)

    setTimeout(function(){
        typeWriter(text,i,0)
    },1000)
    
    

});

// const anchor = document.getElementById('anchor');

// const rekt = anchor.getBoundingClientRect();
// const anchorX = rekt.left + rekt.width/2;
// const anchorY = rekt.top + rekt.height/2;
// const eyes = document.querySelectorAll('.eye')

// document.addEventListener('mousemove',(e) => {
//     const mouseX = e.clientX;
//     const mouseY = e.clientY;

//     const angledeg = angle(mouseX, mouseY, anchorX, anchorY);

//     eyes.forEach(eye => {
//         eye.style.transform = `rotate(${90 + angledeg}deg)`;
//     });
// });

// function angle(cx,cy,ex,ey) {
//     const dy = ey - cy;
//     const dx = ex - cx;

//     const rad = Math.atan2(dy,dx);

//     const deg = rad * 180 /Math.PI;

//     return deg;
// }
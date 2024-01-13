const div = document.querySelector('.pt');
const texta= document.querySelector('.mtext')
const play= document.querySelector('.musi')

const main = document.querySelector('.mainanimation');

setInterval(()=>{
setTimeout(() =>{
    main.style.backgroundImage = "url(' /static/images/m2.png ' )";
    texta.innerHTML="Hyejin Song 🤗";
}, 500)

setTimeout(() =>{
    main.style.backgroundImage = "url(' /static/images/m3.png ' )";
    texta.innerHTML="Shooting Star 🥰 🌠";
}, 4000) }, 10000);



let isClicked=true;

function show() {
    if(isClicked) {
        div.style.display = 'block';
        isClicked = false;
    }else {
        div.style.display = 'none';
        isClicked = true;
    }

}

function show1(){
    div.style.display = 'none';
}



const images = [
    'Assets/Images/bg1.jpg', 'Assets/Images/bg2.jpg', 'Assets/Images/bg3.jpg', 'Assets/Images/bg4.jpg',
    'Assets/Images/bg5.jpg', 'Assets/Images/bg6.jpg', 'Assets/Images/bg7.jpg', 'Assets/Images/bg8.jpg'
];
window.onload = () => {
    // preloading.
    document.body.style.backgroundImage = `url(${images[0]})`;
    document.querySelector('.hidden').src = images[1];
    let i = 1;
    setInterval(() => {
        document.body.style.backgroundImage = `url(${images[i++]})`;
        if(i === images.length) i = 0;
        else {
            //preload the next image, so it transitions smoothly
            document.querySelector('.hidden').src = images[i];
        }
    }, 7000);
}
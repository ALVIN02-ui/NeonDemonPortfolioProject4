// --------------------------------------------------------------------index.html JS
function slideOff() {
    // Function that slides the landing page screen off vertically and loads the new URL
    let landingPage = document.getElementById('landing-page');
    landingPage.style.transform = 'translateY(-100vh)';

    // Access the about URL from the data attribute
    const aboutUrl = document.documentElement.getAttribute('js-about-url');

    setTimeout(() => {
        window.location.href = aboutUrl;
    }, 1000);
}

// --------------------------------------------------------------------about.html JS
document.addEventListener('DOMContentLoaded', function () {
   
    function jumpBetweenImages() {
        //function that jumps between the images in the neon-img container.
        const container = document.querySelector('.about-neon-img');
        const images = container.querySelectorAll('.autoscroll');
        let currentIndex = 0;
        const jumpInterval = 3000; 

        function jumpToNextImage() {
            images[currentIndex].classList.add('hideimg'); 
            currentIndex = (currentIndex + 1) % images.length; 
            images[currentIndex].classList.remove('hideimg'); // Show the next image
        }

        setInterval(jumpToNextImage, jumpInterval); // Jump to the next image at regular intervals
    }

    jumpBetweenImages(); 
});
















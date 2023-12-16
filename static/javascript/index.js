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

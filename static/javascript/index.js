function slideOff() {
    let landingPage = document.getElementById('landing-page');
    let mainContent = document.getElementById('main-content');
    landingPage.style.transform = 'translateY(-100vh)';
    
    setTimeout(() => {
        landingPage.classList.add('hidden');
        mainContent.classList.remove('hidden');
    }, 1000);
}

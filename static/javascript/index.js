const Abouturl = "{% url 'about' %}"

function slideOff() {
    let landingPage = document.getElementById('landing-page');
    let mainContent = document.getElementById('main-content');
    landingPage.style.transform = 'translateY(-100vh)';
    
    setTimeout(() => {
        window.location.href = Abouturl
    }, 1500);
}

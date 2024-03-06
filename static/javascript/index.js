 // ----------------------------------------------------index.html JS
function slideOff() {
    // Function that slides the landing page screen
    // off vertically and loads the new URL
    let landingPage = document.getElementById("landing-page");
    landingPage.style.transform = "translateY(-100vh)";

    // Access the about URL from the data attribute
    const aboutUrl = document.documentElement.getAttribute("js-about-url");

    setTimeout(() => {
        window.location.href = aboutUrl;
    }, 1000);
}

// ----------------------------------------------------about.html JS
document.addEventListener("DOMContentLoaded", function () {
 
    function jumpBetweenImages() {
        //function that jumps between the images in the neon-img container.
        const container = document.querySelector(".about-neon-img");
        const images = container.querySelectorAll(".autoscroll");
        let currentIndex = 0;
        const jumpInterval = 3000;

        function jumpToNextImage() {
            images[currentIndex].classList.add("hideimg");
            currentIndex = (currentIndex + 1) % images.length; 
            // Show the next image
            images[currentIndex].classList.remove("hideimg");
        }
        // Jump to the next image at regular intervals
        setInterval(jumpToNextImage, jumpInterval);
    }

    jumpBetweenImages(); 
});


document.addEventListener("DOMContentLoaded", function () {
    // gets the divs holding the messages and deletes them after 5s
    let messages = document.getElementsByClassName("fadeout");
    messages = Array.from(messages);

    messages.forEach(function (message) {
        setTimeout(function () {
            message.style.display = "none";
        }, 5000);
    });
});

// ----------------------------------------------------------- Gallery.html JS

document.addEventListener('DOMContentLoaded', function() {
    var editButton = document.querySelector('.edit-button');
    var editForm = document.querySelector('.editForm');

    editButton.addEventListener('click', function() {
        if (editForm.style.display === 'none') {
            editForm.style.display = 'block';
        } else {
            editForm.style.display = 'none';
        }
    });
});

// ------------------------------------------------------------Delete confirmation JS
document.addEventListener("DOMContentLoaded", function() {
        
    var modal = document.getElementById("custom-modal");
    var closeModalBtn = modal.querySelector(".close");
    var confirmDeleteBtn = modal.querySelector("#confirm-delete");
    var cancelDeleteBtn = modal.querySelector("#cancel-delete");
    var deleteBtn = document.querySelector(".delete-button");
    var reviewForm = document.getElementById("delete-form");
    var imageForm = document.getElementById("imageForm")

    deleteBtn.addEventListener("click", function(event){
        event.preventDefault();
        modal.style.display = "block"
    });
    
    closeModalBtn.addEventListener("click", function() {
        event.preventDefault();
        modal.style.display = "none"
    });

    cancelDeleteBtn.addEventListener("click", function(event) {
        event.preventDefault();
        modal.style.display = "none"
    });

    confirmDeleteBtn.addEventListener("click", function() {
        
        if (form == reviewForm){
            reviewForm.submit()
            modal.style.display = "none";
        } else if (form == imageForm) {
            imageForm.submit()
            modal.style.display ="none";
        } else {
            alert("Could not process your request")
        }
    });
});






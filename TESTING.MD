# Testing detail

All responsiveness across the entire site has been tested and the entire site works at different breakpoints, having a change in style where necessary to create an optimised UX

## Index.html

### Explore More Button

- Expected: Button on the page slides the screen up and renders the new browser page
  - Tested by clicking the button and checking the action
    - Result: Screen slides up and the new broswer renders.
  
## About.html

### Navbar

- Expected all links in the navbar to work correctly to link to the correct URLs
  - Tested by clicking the links and checking the action and path are correct
    - Result: Each link takes me to the page it is intended too

- Expected the navbar should drop into a button at certain screen sized
  - Tested by reducing the size of the screen in devtools to see when the navbar changes
    - Result: I am pleased with the way the navbar changes to the navbar button at the specified breakpoint

### HeroImage Content

- Expected all links in the main image to work as intended to the correct file paths (mail and messenger)
  - Tested by clicking the links and monitoring the result
    - Result: Both links take me to the intended targets
      - Mail - opens a new email addressed to neon demon
      - Messenger - takes me to a facebook messenger chat to Neon Demon

### Image container

- Expected images within this container autoscroll through the images uploaded into the gallery
  - Tested by uploading new images from all 4 of the users and monitoring the outcome
    - Result: Any images that are uploaded in gallery.html are also displayed in this container with the javascript affecting each one of them, Monitored this on different screen sizes.

### Artist cards

- Expect the view of the cards to change the amount of space they use on different breakpoints
  - Tested by using devtools to monitor the result on different viewports
  - Ran into an issue where the container for these was creating a margin across the right hand side of the screen and large screens as the container was too wide
  - Fixed this by reducing the artist containers to fit 2 columns in bootstrap on large screens and one column on small screens
    - Reult: The margin has disappeared and the site now fits the full width properly on all screens

### Google Map

- Expected the map to render properly in the html file, highlighting the position of the Tattoo Studios location
  - Tested first expectation by opening the webpage on different browsers (Microsoft edge, FireFox and Google Chrome)
    - Result for first expectation: The map renders properly on each of the browsers showing the position of neon demon
- Second expectation the map is interactive to the user and they can use it for directions
  - Tested second expectation by clicking the directions button within the map and monitoring the outcome
    - Result for second expectation the map opens up a new tab asking you to input your location for the direction to the shop

### Footer

- Expected all links contained in the footer to properly connect to the urls they are intended too
  - Tested by clicking all of the links and monitoring the outcome
    - Result: All links take me to the intended urls, opening up in new tabs for new webpages:
      - Messenger
      - Mail
      - Maps
      - Admin page

- Second expectation the 2 divs contained in the footer each take a new line and center on smaller screens
  - Tested by responsively testing the footer on different breakpoints to determine the best one to use to re-arrange the format
    - result the banner and the footer links take up one row each of the footer and move to the center creating the banner above the links for a nice style.

## Gallery.html

### Artist images

#### User

- Expected the images of the artist to appear with a description of their speciality and a link to their gallery
  - Tested by ensuring I was not logged in as any admin and viewed the gallery page as a user
    - Result: The artists images shown as expected with no admin functionality

#### Admin

- Expected the image of the artist I am logged in as to have a form that allows me to upload my images on my picture e.g I am logged in as aaron my picture of aaron should have an upload form
  - Tested by logging in as aaron and monitoring the display view
    - Result: The form appears as expected on the correct image for who is logged in

### Upload Form

- Expected the ability to choose an image, write a short description of the stlye and a clear upload button
  - Tested by logging in as aaron and monitoring the display view
    - Result: The form appears as expected and is responsive based on the viewport

- Expected a feedback message on a successful or unsuccessful upload
  - Tested by uploading an image through each of the admin logins (Aaron, Bran, Danny, Leo)
    - Result: feedback message appears for each of the admins depending on who is logged in

### Gallery Images

#### User

- Expected the ability to browse through gallery photos that are uploaded and if no images a short message saying why
  - Tested by deleting all the images in the gallery and checking the page as no admin
    - Result: The message appears correctly when no images are present
  - Tested by uploading images and checking the page as no admin
    - Result: The images that are successfully uploaded are displayed correctly for the user

- Expected to see on hovering a gallery image the style of the tattoo and who uploaded it
  - Tested by uploading a gallery photo as each superuser and hovering over it
    - Result: The image successfully displays the style of the tattooo and the name of the person who uploaded it

#### Admin

- Expected to have the ability to delete an image from the gallery that I have uploaded
  - Tested by hovering over the image as the uploaded user and checking the button is displayed
    - Result: The image successfully displays the delete button depending on the user who uploaded it.
  
- Expected a feedback message on successful or unsuccessful deletion of a gallery image
  - Tested by deleting an image I have uploaded on each users login
    - Result: The message displays correctly in the artists picture on a successful deletion

- Expected a placeholder for where the next image will be displayed on an upload
  - Tested by removing all images to check the placeholder, Adding imahes to check the placeholder, and viewing where the placeholder sits on different screens
    - Result: The placeholder performs as intended and shows the exact location of the where the next image will be uploaded too.

### Artist pages (aaron.html, bran.html, danny.html, leo.html)

The functionality performs exactly the same on every single one of these pages, I repeated the test steps below for each one of these html pages.

- Expected When an image is uploaded in the gallery that same image also gets moved into the respective artists carousel
  - Tested by logging into each user uploading a photo in the gallery and returning to their personal carousel
    - Result: Images uploaded also get moved into the respective artists carousel

- Expected the carousel automatically moves between images at set intervals, This can also be controlled manually
  - Tested by adding multiple images into the artists gallery and checking the automated and manual aspects of the carousel work
    - Result: Both actions perform as expected, the carousel automates and can be manually controlled.
  
- Expected When an image is uploaded in the gallery that same image also gets moved into the respective artists gallery aswell
  - Tested by logging into each user uploading a photo in the gallery and returning to their personal gallery
    - Result: Images uploaded also get moved into the respective artists gallery

### Review page Before any reviews submitted

- Expected the links to the google review and facebooks review pages to open in a new tab and display the correct content as intended
  - Tested by using admin login to test the links and also as a standard user
    - Result: Both links perform as intended and open in a new page
      - Google - Opens the google reviews page for neondemon in a new tab
      - Facebook - Takes you to the neondemon reviews page on facebook

- Expected a placeholder if no reviews submitted stating so
  - Tested by removing all the reviews and checking if the placeholder exists with nobody logged in and with an admin logged in
    - Result: The placeholder appears when no reviews have been submitted regardless of who is logged in or not.

- Expected the review button to take you to the reviewsform.html page where it displays a form for anybody using the site to fill out
  - Tested by clicking the button on different user accounts and monitoring the outcome
    - Result: In every instance of the testing the outcome always results in the display of the review form.

### ReviewForm

- Expected the review form to be displayed with placeholder text ready to be filled out to leave a review
  - Tested by navigating to the reviews page and checking all the placeholder and the form exists.
    - Result: The form exists and each input field has placeholder to tell you it's purpose.

- Expected the review form to not be submitted if the conditions haven't been met and a message letting the user know why
  - Tested by adding incorrect inputs in the rating field, name field and email field
    - Results:
      - Message displays if rating isn't a number between 1-5 - "Please leave a number between 1-5"
      - Message displays if an input isn't entered into the form - "This field is requires message"
      - Message displays if an email is an incorrect form -"Tells you what is missing from the email for example the '@'"
  
### ReviewForm after submitting a review

- Expected the review page to display the review that has been submitted with the rating, content, name and date submitted
  - Tested by submitting multiple reviews and checking the output on the review page
    - Result: All Reviews display the information that I need for each instance of the review in a clear way ordered from new to old.

- Expected the integer enetered in the review form to be displayed as a star rating on the review page
  - Tested by creating 5 new reviews and checking that each one of them displayed the star rating corresponding to the value
    - Result: All numbers are successfully converted into the appropriate star rating and displayed on the review page.

### 404 page

- Expected when a request is made on the webpage and that page is not found my custom 404 template is displayed
  - Tested by navigating to urls that do not exist in the heroku live deployment
    - The 404 page displays as intented with a button to take you back to about.html

- Expected the button on the 404 page to return me back to the about.html page
  - Tested by using the button in different browsers (Edge, Firefox and Chrome)
    - The button behaves as expected and returns you back to the about.html page.
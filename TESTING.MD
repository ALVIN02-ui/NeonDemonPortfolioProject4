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


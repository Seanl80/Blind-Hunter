# Blind Hunter

## Developer goals

- I would like to build a website which will save the user effort on searching.
- I would like users to be able to benefit from using the website.
- I would like to build a website which is easy to use.
- I would like to make the user able to have their own profile for when they use the website.

## User goals

- I want to easily search and find what I am looking for.
- This website should be easy to navigate without being confusing.
- I would like the users to easily identify why they would benefit from using the site.
- Users should feel they want to use the site as often as possible to benefit them.

## User stories

As a user of this quiz, I want:

- To be able to easily navigate through the website.
- To be able to benefit from using this website.
- To know what the next steps are to contact companies.
- To be able to create a new profile.
- To be able to log back in as myself to leave new reviews and get discounts.

## Design choices

- The basic colour range for this quiz are with the following colours :-
- ![#ffffff](https://placehold.co/15x15/ffffff/ffffff.png) `#ffffff`
- ![#455a64](https://placehold.co/15x15/455a64/455a64.png) `#455a64`
- ![#795548](https://placehold.co/15x15/795548/795548.png) `#795548`
- ![#00c853](https://placehold.co/15x15/00c853/00c853.png) `#00c853`
- ![#000000de](https://placehold.co/15x15/000000de/000000de.png) `#000000de`
- ![#f44336](https://placehold.co/15x15/f44336/f44336.png) `#f44336`
- ![#26a69a](https://placehold.co/15x15/26a69a/26a69a.png) `#26a69a`

- I chose these colours as they are fashionable colours for blinds.
- I chose green and red for button navigation as they are universally recognised.
- I felt these colours blended well to make an appealling website.

## Wireframes

Here are the original wireframes:

![Home page wireframe](https://github.com/Seanl80/MS3/blob/main/blindhunter/static/wireframes/blind-project-wire-frames.pdf)
![Companies page wireframe](static/wireframes/companies-page.png)
![Reviews wireframe](static/wireframes/reviews-page.png)

---

## Existing features


---

## Technologies used

- For this website I have chosen to use HTML, CSS and JavaScript.
- I have also used Python and Postgresql.
- I have also included Materialize.
- Gitpod was used as my IDE.
- GitHub was used to store my code.
- Heroku was used to deploy the website.

---

## Testing

I have used these validators to check the validity of my code.

- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)


- [W3C Markup Validation](https://validator.w3.org/)


- [JShint JavaScript Validation](https://jshint.com/)


## Testing Developer Goals


## Testing User Stories


---

## Bugs

## Deployment

This project was developed using the [Gitpod IDE](https://https://gitpod.io/). Then developments and changes were commited and pushed to GitHub.

To clone this project into Gitpod you will need:

1. A GitHub account. [Create a GitHub account here](https://www.github.com).
2. Use the Chrome browser.

Then follow these steps:

1. Install the Gitpod Browser Extensons for Chrome.
2. After installation restart the browser.
3. Log into Gitpod with your Gitpod account.
4. Navigate to the Project GitHub repository.
5. Click the green "Gitpod" button in the top right of the repository.
6. This will trigger a new gitpod workspace to be created from the code in github where you can work locally.

To deploy this page from Heroku, the following steps were taken:

1. Type pip3 freeze --local > requirements.txt into the Gitpod terminal to create a requirements.txt file.
2. Type echo web: python app.py > Procfile into the terminal to create a Procfile.
3. Commit and push the changes to GitHub.
4. Create a Heroku Account and log in.
5. Click 'New' -> 'Create new app'.
6. Enter a name for your project and select your region.
7. Click 'Create app'.
8. Go to 'Settings', click 'Reveal Config Vars'.
9. Add the following variables:
- DATABASE_URL: your ElephantSQL database url
- IP: 0.0.0.0
- PORT: 5000
- SECRET_KEY: your secret key
- DEBUG: True
10. Click on the 'Deploy' tab.
11. Click 'Connect to GitHub'.
12. Find your repo and click 'Connect'
13. Click 'Deploy Branch'.
14. Click 'More' -> 'Run console'
15. Type in python3
16. Type from blindhunter import db -> db.create_all() -> exit().
17. Click 'Open App'.

---

## Credits

### Code

My thanks go out to tutors Sarah and John at Code institue for their assistance in problems.



### Media

- For my image I used [Freepik](https://www.freepik.com/).
- For my favicon image I used [Icon Archive](https://www.iconarchive.com/show/sleek-xp-basic-icons-by-hopstarter/Money-icon.html).
- To show my website on different screens I used [Am I responsive](https://ui.dev/amiresponsive/) to create them.
- For my wirefreames I used [Balsamiq](https://balsamiq.com/).



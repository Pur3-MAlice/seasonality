# **Season to Taste**
This website has been built as a digital cookbook. Where people can upload their own recipes, comment, favourite and rate other people's submissions (including the admin's). This website aims to target the lack of community and collaboration within recipe websites. User submission give user a level of control, whilst the admin is also in charge of making sure the community is staying safe. It also aims to tackle the preamble that comes before recipes on websites that people find annoying, even if it is good SEO.

As a notice here - this is the second version of this app I made. The first version had many errors and it was early on in the development project that creating a new repo at that point was the best option. Here is the link to the old repo, [Season-To-Taste](https://github.com/Pur3-MAlice/season-to-taste/tree/main) it has the same Kanban Board and also lots of commits that should be noted.

![Responsive screenshot at Desktop]()

![Responsive screenshot at Laptop]()

![Responsive screenshot at Tablet]()

![Responsive screenshot at Mobile]()

[Deployed site]()

# **Table Of Contents**
* [**Season-to-Taste**](#season-to-taste)
* [**Planning Phase**](#planning-phase)
    * [**Site Aims**](#site-aims)
    * [**Epics User Stories Tasks**](#epics-user-stories-tasks)
    * [**Research**](#research)
    * [**Skeleton**](#skeleton)
    * [**Surface**](#surface)
* [**Agile Development Process**](#agile-development-process)
* [**Future development**](#future-development)
* [**Features**](#features)
  * [**Site Navigation**](#site-navigation)
  * [**Signin/up Logout Pages**](#signin/up-logout-pages)
  * [**Community Guidelines**](#community-guidelines)
  * [**Main Page Content**](#main-page-content)
  * [**Error pages**](#error-pages)
* [**Testing Phase**](#testing-phase)
* [**Deployment**](#deployment)
* [Credits](#credits)

# **Planning Phase**
## **Site Aims:**
The site aims to:
* Create community minded website that can share, favourite, rate and create recipes to create their own digital cookbook.
* Tell the user if they have made any errors whilst using the website and prompt them as such.
* Give user a lot of control with creation of content. Whilst Admin approves and can remove content that goes against guidelines to promote the community spirit.

How Will This Be Achieved:
To achieve the above, the site will:
* Create environment that focuses on sharing own ideas, thoughts whilst also ensuring community guidelines are stuck to.
* User submission and editing of their own recipe submissions, their own favourite lists and own ratings.
* Author ability to delete and edit their own recipes whenever they would like. Delete function has fail safes incase of mis-type.
* User validation via error messages.

## **Epics User Stories Tasks**
I took the site aims from the above and turned them into Epics, User Stories and then Tasks. Find below a break down of the three Epics and their User Stories/Tasks.

**Epic 1: Recipe Management**

User Stories:
* As a **Site User**, I can submit my own recipes to the admin so that approved recipes can be added to the site.
* As a **Site User**, I can change my ratings and saved recipes so that I can reflect how my preferences may change.
* As a **Site User**, I can save recipes to my own 'digital cookbook' so that I can easily access all my favorite recipes.
* As a **Site User**, I can comment on recipes so that I can join in with the community and make suggestions.
* As a **Site User**, I can search recipes on the site by title, diet, season, author, and ingredients so that I can find recipes to my liking.

Tasks:
1. Implement recipe submission functionality.
1. Implement recipe rating and updating functionality.
1. Implement the ability to save recipes to a user's profile.
1. Implement commenting on recipes.
1. Implement search functionality with title, diet, season, author, and ingredients.

**Epic 2: Community Guidelines and User Sign-in/Sign-up**

User Stories:
* As a **Site User**, who hasn't yet logged in/up I can sign in/sign up so that I can access features non-signed-in members can't.
* As a **Site User**, I can get access to the community guidelines so that I can understand how to appropriately join in with the community.

Tasks:
1. Implement user authentication and sign-up/sign-in functionality.
1. Provide access to community guidelines for all users.

**Epic 3: Admin Control**

User Stories:
* As an **Admin**, I can draft recipes so that I can control the website's content and when content will be added to the site.
* As an **Admin**, I can CRUD recipes and comments so that I can control the site's content to be in line with community guidelines.
* As an **Admin**, I can approve or disapprove recipe submissions and recipe edits so that I can control the website content.

Tasks:
1. Implement the ability for admins to draft recipes.
1. Implement admin controls for CRUD operations on recipes and comments.
1. Implement filtering through the admin panel to see all comments and recipes. 

Here is how I broke these down into the Must, Should and Could Haves for this project.

![Must Should Could](/documents/agile/must-should-could.png)

And here is a progression of my Kanban Board
![Kanban Board 1](/documents/agile/starting%20kanban%20board.png)

![Kanban Board 2](/documents/agile/mid-build%20kanban%20board.png)

![Kanban Board 3](/documents/agile/mid-build-kanban-board.2.png)

![Kanban Board 4](/documents/agile/mid-build-kanban-board.3.png)

![Kanban Board 5](/documents/agile/mid-build-kanban-board.4.png)

## **Research:**
One of the first things I did when building the plan for this website was research. I wanted my website, not only to be useable and have a solid logic base but for it also to look modern and inviting. So part of my Planning Phase was not only wireframing, building a logic flow chart and a database schema. But also looking at websites with similar aims, and discussing with friends and family how they use recipe websites. What do they like, what do they dislike, and how can I emulate the good parts whilst removing the annoyance? One thing that did keep popping up is the blog post before the recipe, which for this site is not applicable. The user can submit content that is longer, but unless this breaches the guidelines this is the user's content and therefore will be posted. However due to the community and edit aspect of this website, content can be change upon the community calling for it. The beauty of this site is that the community of users will decide the accpeted formula, which is what is missing in traditional recipe websites. 

Here are some of the sites I used for inspiration for the design of Season To Taste:
* [thehappyfoodie](https://thehappyfoodie.co.uk/)
* [cookbookmanager](https://cookbookmanager.com/pricing)
* [Resturant Website Templates from Wix](https://www.wix.com/website/templates/html/restaurants-food)

## **Skeleton**
### **Wireframes:**
![Home Page Desktop](/documents/wireframes/desktop-home.png)

![Profile Page Desktop](/documents/wireframes/desktop-profile.png)

![Recipe Page Desktop](/documents/wireframes/desktop-recipe.png)

![Home Page Tablet](/documents/wireframes/tablet-home.png)

![Profile Page Tablet](/documents/wireframes/tablet-profile.png)

![Recipe Page Tablet](/documents/wireframes/tablet-recipe.png)

![Home Page Mobile](/documents/wireframes/mobile-home.png)

![Profile Page Mobile](/documents/wireframes/mobile-profile.png)

![Recipe Page Mobile](/documents/wireframes/mobile-recipe.png)

### **Database Schema**
Below is my initial database schema to map out the relations between users, recipes, comments and categories (also known as tags). This is a rough idea of what the database will look like in general, but at this point in the planning phase, I understand that this is subject to change. 
![Database Scheme](/documents/wireframes/db-schema.png)
On the completion of this project, this database, while it does differ in some areas, is pretty much how my datbase structure has gone. Which I am happy with. 

My database is structured at deployment with two main apps which are connected to each other. The recipebook app and the profile app. The recipebook model holds the recipe database which controls the functionality of each individual recipe, each category (diet and season), and the ratings. This is then connected to the profile through the user interface as the user will input on the page. This is part of the website's MVT, say the model of recipe is being passed into the RecipeDetail view and then the user will see the recipe_detail template. This is displayed. The database was extended from the original schema to also include profile elements which would allow the user to properly store their own favourties and access/edit/delete their recipe inputs. 

When it came to actually putting my Database Schema into reality a few things changed. Such as Saved and Categories. Plus I figured out I would need to make a model purely for the rating system I wanted to put in place. MVP this could just be likes, but to differentiate from the base of this project (which was taken from Code Insitutes 'Django Blog App') I wanted to add in this rating system that would calculate a recipes' popularity. This would also be the building block of the carousels on the recipe search page. I plan to have 'Diet' and even 'Season' Caraousels on the recipe search page so that site users can easily see recipes, the rating system will determine which recipes show up on these carousels. Or So I Plan... (Famous last words of a coder).
 
## **Surface**
### **Color scheme:**
I knew I wanted my main theme to be pink and mustard as they are very in vouge right now. So i used this article https://www.thespruce.com/complementary-colors-that-go-with-pink-5188287 and then used https://coolors.co/f1cacc-df8a70-e8ac33-5a6950-13322c to create my colour Palatte

The final list of colors used has been placed in the below to check contrast scores.

![Color Scheme](/documents/wireframes/color-scheme.png)

![Color Grid](/documents/wireframes/contrast-grid.png)

### **Typography**:
To find my fonts i used thsi website: https://www.elegantthemes.com/blog/design/best-google-fonts. I went with Playfair Display and Monserrat, for a modern playful feel that would give the website levity.

# **Agile Development Process**
Using a Kanban Board system

# **Future development**
1. I think that the ability to like and reply to other comments in the future would be a good addition to the site based on its aims.
1. For the user to be able to develop more than one list of favourites, like playlists of recipes.
1. I would also like for the users to be able to report recipes and comments to admin, or have a way of getting in touch with admin for site regulation.

The future development of this project would also to improve the user's inputs and needs. By changing the ingridient list to a checkbox list. Editing the serv's per recipe and then editing the ingridient amounts. Adding in cook time and cook complexity too. Overall just improving the user's ability to adapt a recipe on the site to their own needs. 
# **Features**
## **Site Navigation**
### ***Signed Out:***
![sign-out nav](/documents/features/signout-nav.png)
#### ***Signed In:***
![sign-in nav](/documents/features/signin-nav.png) 

### **Signin/up Logout Pages**

### **Community Guidelines**

### **Main Page Content**

### **Add/Update Recipe Forms**

![add recipe](/documents/features/add-recipe.png)

![update recipe](/documents/features/update-recipe.png)

### **Recipe Detail**

### **Search**

### **Error pages**
**Sign In:**
![sign-in form](/documents/features/signout-nav.png)
**Form Errors:**
![sign-in error](/documents/features/sign-inerror.png)
**Sign Up:**
![sign-up form](/documents/features/register.png) 

As described in the testing below - more errors are tried and tested with these forms and the other forms on the website.
**Form Errors:**
![sign-up error](/documents/features/sign-uperror.png)

As described in the testing below - more errors are tried and tested with these forms and the other forms on the website.
**Sign Out:**
![Sign out page](/documents/features/signout.png)

1. Change password and Delete Profile
# **Testing Phase**
### ***Manual Testing:***
During the development process, I was manually testing in the following ways:-
* Manually testing each element for appearance and responsiveness via a simulated live server using an extension in VSCode.
* Used the terminal to find errors when saving and psuhing to dev server.
* Asked a Data Scientist friend to review the pages and the websites responsiveness by following the above procedure often throughout the development of the site. They did not offer any help on the coding nor did they provide feedback other than "this link/button/card" is broken. They did however make a good soundboard for me to talk at while talking through difficult code issues. Below is the spreadsheet I used for user testing.

Logged in 

![Logged in Nav](/documents/testing/Logged%20in%20NavBar.png)

![Logged in Add Recipe](/documents/testing/Logged%20in%20Add%20Recipe.png)

![Logged in Add Fav](/documents/testing/Logged%20in%20Favourites%20Page.png)

![Logged in Home Page](/documents/testing/Logged%20in%20Homepage.png)

![Logged in Profile](/documents/testing/Logged%20in%20Profile%20page.png)

![Logged in Recipe Page](/documents/testing/Logged%20in%20Recipe%20Page.png)

![Logged in Searched](/documents/testing/Logged%20in%20Searched%20Page.png)

![Logged in Signout](/documents/testing/Logged%20in%20Signout%20Page.png)

![Logged in Update Page](/documents/testing/Logged%20in%20Update%20Recipe.png)

Logged out

![Logged out Nav](/documents/testing/Not%20Logged%20in%20NavBar.png)

![Logged out Home Page](/documents/testing/Not%20Logged%20in%20Home%20Page.png)

![Logged out Login](/documents/testing/Not%20Logged%20in%20Login%20Page.png)

![Logged out Register](/documents/testing/Not%20Logged%20in%20Register%20Page.png)

![Logged out Recipe Page](/documents/testing/Not%20Logged%20in%20Recipe%20Page.png)

![Logged out Searched](/documents/testing/Not%20Logged%20in%20Search%20Page.png)

![Logged out Signout](/documents/testing/Logged%20in%20Signout%20Page.png)

### ***Bugs and Fixes:***
Below is a list of bugs I found during the development process. A lot of the bugs and fixes where minor enough that they were caught and easily amended by just seeing the redlines in gitpod. But here are a few that stumped me enough to write them down.
1. **Intended Outcome** - I could start my project and continue to use the same repository.
    * ***Issue Found:*** 
        * Due to some database issues I could not migrate any changes after I had done my first migration.
    * ***Solution Used:*** 
        * Restarted the project and used db.sqlite3 instead of my main postgres db, and implemented a DEV environment.
1. **Intended Outcome** - Only have certain number of diet categories on the home page.
    * ***Issue Found:*** 
        * I wanted to only have three of my categories on the main page, I ended up aving all the categories being listed out on the front page which isn't good UI/UX.
    * ***Solution Used:*** 
        * Discovered I could splice in the django html templates.
1. **Intended Outcome** - Be able to search entire db for recipes and their FKs
    * ***Issue Found:*** 
        * I wanted to be able too not only search the content of the recipes in the search bar but also search if they were connected to the FK.
    * ***Solution Used:*** 
        *   i discovered I could use the Q search to see if what FKs were connected to which recipe. Meaning that the user can search categories and get all recipes related to that category shown back to them.
1. **Intended Outcome** - Be able to rate a recipe and have my rating remembered on the UI whilst also updating the rating average.
    * ***Issue Found:*** 
        * The avg of the recipe page would be affected. But the user input of the stars themselves would not hold the data.
    * ***Solution Used:*** 
        *  Used Javascript local storage to hold the browsers star rating instead. However this does leave an error in the console, the benefit of the user's rating being remebered is not outweighed by this as it does not affect the page's functionality or the user's experience. 
1. **Intended Outcome** - When deploy to heroku the CSS stay's connected
    * ***Issue Found:*** 
        * CSS Styling not coming and getting console error of MIME.
    * ***Solution Used:*** 
        * Removed DISABLE_COLLECTSTATIC and PORT 8000 and then the CSS styling worked.

* During testing, I used three browsers to ensure cross-compatibility. The browsers used were:
  1. Chrome
  2. Firefox  
  4. Edge
* I also consistently used the devtools to simulate different screen sizes/devices from 320px up to 2200px in width. 
* In addition to this, I used the dev tools to simulate different products such as the iPhone XR, iPhone 12 Pro, Samsung Galaxy S8+, iPad Air, iPad Mini, Surface Pro 7 and Nest Hub.
* I also got friends and my partner to test the site on their own devices - Samsung, Dell Laptops, Self-built desktops and Apple products. 

![HTML validator](/documents/html%20validator.png)

#### ***CSS*** - https://jigsaw.w3.org/css-validator/
* Code passes through with no issues.

![CSS badge](/documents/css%20validator.png)

* I also passed the code through a jshint and PEP8 with no issues. 

# **Deployment**
## ***Final Deployment to Heroku:***  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. Log in to Heroku
1. Click the button labelled "New”.
1. From the drop-down menu select "Create new app".
1. Enter a unique app name.
1. Once the web portal shows the green tick to confirm the name is original.
1. Select the relevant region, I chose Europe as I am in the UK.
1. Click on the "Create app" button.
1. From the project "Deploy" tab, nav to the settings tab and scroll to the "Config Vars" section. 
1. Click the button labelled "Reveal Config Vars" and enter port / 8000. Click the "add" button. (This was later removed for the static file issue, but should usually be done for deployment.)
1. Scroll to the top of the settings page, and nav to the "Deploy" tab.
1. From the deploy tab select Github as the deployment method.
1. Confirm you want to connect to GitHub.
1. Search for the repo and click the connect button.
1. From the bottom of the deploy page select your preferred deployment type by follow one of the below steps:  
   * Clicking “Enable Automatic Deploys" for automatic deployment when you push updates to Github.
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.

# Credits
* General references:
* Whilst I did try to deviate as much as possible, this project was influenced by the CI code project which I built before starting this project.
* Figma was used to create the wireframes.
* The site was developed using Gitpod.
* GitHub was used to store my repository.
* [Article Epics and how to make them](https://www.atlassian.com/agile/project-management/epics#:~:text=Epics%20are%20an%20important%20practice,of%20customers%20or%20end%2Dusers.)
* [coolers.co](https://coolors.co/603f3f-a0acca-e4b67c-de9f13-000000) was used to generate color scheme.
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* Images:
  * Recipe images taken from [upsplash.com](https://unsplash.com) 
  * Background image designed by me in Canva.
* For this project I researched lots of other Django projects. Through other tutorials I learned more about how to properly utlise all of Django's capabilities. Some code in this project has been inspired by these walkthroughs, although significant changes have been made to ensure that the code works with and for this specific Django App. Here is a comprehensive list of YouTube Pages that helped this project come to life.
    * [@Codemycom](https://www.youtube.com/@Codemycom)
    * [@DigitalFox-tutorials](https://www.youtube.com/@DigitalFox-tutorials)
    * [@Pyplane](https://www.youtube.com/@Pyplane)
    * [@veryacademy)](https://www.youtube.com/@veryacademy)
* General references:
    * [Stack Overflow](https://stackoverflow.com/)
    * [Code Institute Learning Platform](https://codeinstitute.net/)
    * [Django Documentation](https://docs.djangoproject.com/en/3.2/)
    * [Bootstrap Documentation](https://getbootstrap.com/)
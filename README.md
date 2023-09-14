# **Season to Taste**
[Seasonality](https://seasonality-c30a72c679d8.herokuapp.com/)

This website has been built as a digital cookbook. Where people can upload their own recipes, comment, favourite and rate other people's submissions (including the admin's). This website aims to target the lack of community and collaboration within recipe websites. User submission gives the user a level of control, whilst the admin is also in charge of making sure the community is staying safe. It also aims to tackle the preamble that comes before recipes on websites that people find annoying, even if it is good SEO.

As a notice here - this is the second version of this app I made. The first version had many errors and it was early on in the development project that creating a new repo at that point was the best option. Here is the link to the old repo, [Season-To-Taste](https://github.com/Pur3-MAlice/season-to-taste/tree/main) it has the same Kanban Board and also lots of commits that should be noted.

![Responsive screenshot](/documents/responsive-image.png)

# **Table Of Contents**
* [**Season-to-Taste**](#season-to-taste)
* [**Planning Phase**](#planning-phase)
    * [**Site Aims**](#site-aims)
    * [**Epics User Stories Tasks**](#epics-user-stories-tasks)
    * [**Kanban Agile**](#kanban-agile)
    * [**Research**](#research)
    * [**Skeleton**](#skeleton)
    * [**Surface**](#surface)
* [**Future development**](#future-development)
* [**Features**](#features)
  * [**Site Navigation**](#site-navigation)
  * [**Sign in**](#sign-in)
  * [**Register Page**](#register-page)
  * [**Sign Out Page**](#sign-out-page)
  * [**Community Guidelines Modal**](#community-guidelines-modal)
  * [**Search**](#search)
  * [**Profile Features**](#profile-features)
  * [**Favourites Page**](#favourites-page)
  * [**Add/Update Recipe Forms**](#add/update-recipe-forms)
  * [**Recipe Detail**](#recipe-detail)
  * [**Commenting**](#commenting)
* [**Error pages**](#error-pages)
* [**Testing Phase**](#testing-phase)
* [**Deployment**](#deployment)
* [**Credits**](#credits)

# **Planning Phase**
## **Site Aims:**
The site aims to:
* Create community community-minded website that can share, favourite, rate and create recipes to create their own digital cookbook.
* Tell the user if they have made any errors whilst using the website and prompt them as such.
* Give users a lot of control over the creation of content. Whilst Admin approves and can remove content that goes against guidelines to promote the community spirit.

To achieve the above, the site will:
* Create an environment that focuses on sharing own ideas, and thoughts whilst also ensuring community guidelines are stuck to.
* User submission and editing of their own recipe submissions, their own favourite lists and their own ratings.
* Author ability to delete and edit their own recipes whenever they would like. The delete function has fail-safes in case of mistypes.
* User validation via error messages.

## **Epics User Stories Tasks**

I took the site aims from the above and turned them into Epics, User Stories and then Tasks. Find below a breakdown of the three Epics and their User Stories/Tasks.

**Epic 1: Recipe Management**

User Stories:
* As a **Site User**, I can submit my own recipes to the admin so that approved recipes can be added to the site.
* As a **Site User**, I can change my ratings and saved recipes so that I can reflect how my preferences may change.
* As a **Site User**, I can save recipes to my own 'digital cookbook' so that I can easily access all my favourite recipes.
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

## ***Kanban Agile***
And here is a progression of my Kanban Board
![Kanban Board 1](/documents/agile/starting%20kanban%20board.png)

![Kanban Board 2](/documents/agile/mid-build%20kanban%20board.png)

![Kanban Board 3](/documents/agile/mid-build-kanban-board.2.png)

![Kanban Board 4](/documents/agile/mid-build-kanban-board.3.png)

![Kanban Board 5](/documents/agile/mid-build-kanban-board.4.png)

## **Research:**
One of the first things I did when building the plan for this website was research. I wanted my website, not only to be useable and have a solid logic base but for it also to look modern and inviting. So part of my Planning Phase was not only wireframing, building a reasonable and logical database schema. But also looking at websites with similar aims, and discussing with friends and family how they use recipe websites. What do they like, what do they dislike, and how can I emulate the good parts whilst removing the annoyance? One thing that kept popping up was the blog post before the recipe, which for this site is not applicable. The user can submit content that is longer, but unless this breaches the guidelines this is the user's content and therefore will be posted. However, due to the community and editing aspect of this website, content can be changed upon the community calling for it. The beauty of this site is that the community of users will decide on the accepted formula, which is what is missing in traditional recipe websites. 

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

On the completion of this project, this database, while it does differ in some areas, is pretty much how my database structure has gone. Which I am happy with. 

My database is structured at deployment with two main apps which are connected to each other. The recipebook app and the profile app. The recipebook model holds the recipe database which controls the functionality of each individual recipe, each category (diet and season), and the ratings. This is then connected to the profile through the user interface as the user will input on the page. This is part of the website's MVT, say the model of a recipe is being passed into the RecipeDetail view and then the user will see the recipe_detail template. This is displayed. The database was extended from the original schema to also include profile elements which would allow the user to properly store their own favourites and access/edit/delete their recipe inputs. 

When it came to actually putting my Database Schema into reality a few things changed. Such as Saved and Categories. Plus I figured out I would need to make a model purely for the rating system I wanted to put in place. MVP could just be 'likes', but to differentiate from the base of this project (which was taken from Code Institutes' 'Django Blog App') I wanted to add in this rating system that would calculate a recipe's popularity. This would also be the building block of the carousels on the recipe search page. I plan to have 'Diet' and even 'Season' Caraousels on the recipe search page so that site users can easily see recipes, the rating system will determine which recipes show up on these carousels. Or So I Plan... (Famous last words of a coder).
 
## **Surface**
### **Color scheme:**
I knew I wanted my main theme to be pink and mustard as they are very in vogue right now. So I used this article https://www.thespruce.com/complementary-colors-that-go-with-pink-5188287 and then used https://coolors.co/f1cacc-df8a70-e8ac33-5a6950-13322c to create my colour Palette

The final list of colours used has been placed below to check contrast scores.

![Color Scheme](/documents/wireframes/color-scheme.png)

![Color Grid](/documents/wireframes/contrast-grid.png)

### **Typography**:
To find my fonts I used this website: https://www.elegantthemes.com/blog/design/best-google-fonts. I went with Playfair Display and Monserrat, for a modern playful feel that would give the website levity.

# **Future development**
1. For the user to be able to change their password and delete their profile.
1. I think that the ability to like and reply to other comments in the future would be a good addition to the site based on its aims.
1. For the user to be able to develop more than one list of favourites, like playlists of recipes.
1. I would also like for the users to be able to report recipes and comments to admin or have a way of getting in touch with admin for site regulation.

The future development of this project would also improve the user's inputs and needs. By changing the ingredient list to a checkbox list. Editing the serv's per recipe and then editing the ingredient amounts. Adding in cook time and cook complexity too. Overall just improves the user's ability to adapt a recipe on the site to their own needs. 

# **Features**
## ***Site Navigation***
Below are the screenshots of both the logged-in version of the nav bar and the logged-out version. As you can see when a user logs in they get access to the profile drop down 
### ***Search Bar for Both:***
![search bar](/documents/features/search-bar.png) 
### ***Signed Out:***
![sign-out nav](/documents/features/signout-nav.png)
### ***Signed In:***
![sign-in nav](/documents/features/signin-nav.png) 
## ***Sign in Page***
![sign-in page](/documents/features/signin.png) 
## ***Register Page***
![register page](/documents/features/register-page.png) 
## ***Sign Out Page***
![Sign out page](/documents/features/signout.png)
## ***Community Guidelines Modal***
This is the same modal across all pages, logged in or out. 

![Community Modal](/documents/features/community-modal.png)

## ***Search***

Here is a search with no results, it gives the user a message saying they didn't search anything and then also prompts them to make a suitable search.

![Empty Search](/documents/features/search-nothing.png)

Here is a page pagination. I searched a term with more than 8 results and got the below, which means I see the pagination that lets me go through all the results.

![Large Search](/documents/features/search_large.png)

This is a search for an ingredient so only shows up one result with that specific ingredient. Here you can see that there is no pagination due to the results being less than 8.

![Specific Search](/documents/features/searched-ingredient.png)

## ***Main Page Content***

This is a view of the main page content. You can see here the left and right chevron as this is the second row of the recent recipe list. This list is paginated by 4 and after each 4 recipes, the next recipe goes unto the next row. You can also see the start of the diet lists, which is maxed out at three diets on the home page. These also populate with the latest additions to these diets. 

![Main Page](/documents/features/main-page-chevron.png)

## ***Profile Features***

Below is the profile, which has features such as a link to the favourites page, a button to remove the recipe from favourites, and update and delete recipes from db if author. And a feature to update the user's bio, username and email. 

![Full Profile](/documents/features/profile-page.png)

![My Recipes](/documents/features/my-recipes.png)

![My Favourties](/documents/features/my-favourites.png)

## ***Favourties Page***

This is a full page of the user's favourites i.e. their digital cookbook, where they can also remove the recipes very easily. 

![Favourties Page](/documents/features/favourite-page.png)

## ***Add/Update Recipe Forms***

Below are images of the Add recipe and Update recipe form. They are formatted the same apart from two distinctions, only the author of the recipe can access the updated recipe form for a specific recipe ID, and the update recipe form is already up to date with the current recipe content. Excluded from these forms is the slug field, which is automatically generated through javascript code, the favourites list which should only be affected by other users adding or removing the recipe from their own favourites/digital cookbook, and the author which is also automatically applied as the logged in user == the author of the recipe.

![add recipe](/documents/features/add-recipe.png)

![update recipe](/documents/features/update-recipe.png)

## ***Recipe Detail***

* Logged in: The logged-in user here can view and interact with the recipe. They can rate, favourite and comment on this recipe as seen in the image below.

![Logged in Recipe Detail](/documents/features/recipe-detail-none-author-view-logged-in.png)

* Logged out: The logged-out user here can only view the average rating, the comments and the fav button. When they click on the fav button they get taken to the registration page. This is done as the site's aim is to get users to sign up, by showing them one feature that they would most likely interact with and then taking them to a reg page, the user is more likely to sign up. The site's aims are supported by this feature. 

![Logged out Recipe Detail](/documents/features/recipe-detail-loggedout.png)

* Author Logged in: The logged in user who is also the author can view and interact with the recipe in a more substantial way. They can rate, fav and comment on this recipe as seen in the image below, but they can also update and delete the recipe.

![Logged out Recipe Detail](/documents/features/recipe-detail-author-view.png)

## ***Commenting***

* Logged Out: The logged out user here can only view comments and click register to create a profile adn eventually comment on the post. 

![Logged out Recipe Comments](/documents/features/comments-logged-out.png)

* Logged in: The logged in user here can view and comment on the recipe with feedback, suggestions and help create a community atmosphere. The user will also get a refresh and a notification of successful comment.

![Logged in Recipe Comments](/documents/features/comments-logged-in.png)

![Logged in Recipe Comments Success](/documents/features/comment-posted.png)

# **Error pages**
**Sign In:**

![sign-in error](/documents/features/errors/sign-in-error.png)

![sign-in password error](/documents/features/errors/sign-in-password-error.png)

**Registration:**

![Registration email error](/documents/features/errors/register-email-error.png)

![Registration password empty](/documents/features/errors/register-password-empty-error.png) 

![Registration password match](/documents/features/errors/register-password-match-error.png) 

![Registration password other](/documents/features/errors/register-password-other-errors.png)

![Registration short error](/documents/features/errors/register-password-short-error.png) 

**Profile Updating:**

![Profile detail email error](/documents/features/errors/profile-details-formerror-email.png)

![Profile detail form error](/documents/features/errors/profile-details-formerror.png) 

**Add Recipe Errors:**

![Add Recipe Errors](/documents/features/errors/recipe-add-errors.png)

**Update Recipe Errors:**

![Update Recipe Errors](/documents/features/errors/update-errors.png)

**Comment Errors:**

![Comment Error](/documents/features/errors/comment-error.png)

# **Testing Phase**
### ***Manual Testing:***
During the development process, I was manually testing in the following ways:-
* Manually testing each element for appearance and responsiveness via a simulated live server using an extension in VSCode.
* Used the terminal to find errors when saving and psuhing to dev server.
* Asked a Data Scientist friend to review the pages and the websites responsiveness by following the above procedure often throughout the development of the site. They did not offer any help on the coding nor did they provide feedback other than "this link/button/card" is broken. They did however make a good soundboard for me to talk at while talking through difficult code issues. Below is the spreadsheet I used for user testing.

Logged in:

![Logged in Nav](/documents/testing/Logged%20in%20NavBar.png)

![Logged in Add Recipe](/documents/testing/Logged%20in%20Add%20Recipe.png)

![Logged in Add Fav](/documents/testing/Logged%20in%20Favourites%20Page.png)

![Logged in Home Page](/documents/testing/Logged%20in%20Homepage.png)

![Logged in Profile](/documents/testing/Logged%20in%20Profile%20page.png)

![Logged in Recipe Page](/documents/testing/Logged%20in%20Recipe%20Page.png)

![Logged in Searched](/documents/testing/Logged%20in%20Searched%20Page.png)

![Logged in Signout](/documents/testing/Logged%20in%20Signout%20Page.png)

![Logged in Update Page](/documents/testing/Logged%20in%20Update%20Recipe.png)

Logged out:

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
        * Restarted the project and used db.sqlite3 instead of my main Postgres db, and implemented a DEV environment.
1. **Intended Outcome** - Only have a certain number of diet categories on the home page.
    * ***Issue Found:*** 
        * I wanted to only have three of my categories on the main page, I ended up having all the categories listed on the front page which isn't good UI/UX.
    * ***Solution Used:*** 
        * Discovered I could splice in the Django html templates.
1. **Intended Outcome** - Be able to search the entire db for recipes and their FKs
    * ***Issue Found:*** 
        * I wanted to be able too not only search the content of the recipes in the search bar but also search if they were connected to the FK.
    * ***Solution Used:*** 
        *   I discovered I could use the Q search to see what FKs were connected to which recipe. Meaning that the user can search categories and get all recipes related to that category shown back to them.
1. **Intended Outcome** - Be able to rate a recipe and have my rating remembered on the UI whilst also updating the rating average.
    * ***Issue Found:*** 
        * The average of the recipe page would be affected. However the user input of the stars themselves would not hold the data.
    * ***Solution Used:*** 
        *  Used Javascript local storage to hold the browser's star rating instead. However this does leave an error in the console, the benefit of the user's rating being remembered is not outweighed by this as it does not affect the page's functionality or the user's experience. 
1. **Intended Outcome** - When deploying to Heroku the CSS styling stays attached to the website.
    * ***Issue Found:*** 
        * CSS Styling not coming and getting console error of MIME.
    * ***Solution Used:*** 
        * Removed DISABLE_COLLECTSTATIC and PORT 8000 and then the CSS styling worked.

* During testing, I used three browsers to ensure cross-compatibility. The browsers used were:
  1. Chrome
  2. Firefox  
  4. Edge
* I also consistently used the dev tools to simulate different screen sizes/devices from 320px up to 2200px in width. 
* In addition to this, I used the dev tools to simulate different products such as the iPhone XR, iPhone 12 Pro, Samsung Galaxy S8+, iPad Air, iPad Mini, Surface Pro 7 and Nest Hub.
* I also got friends and my partner to test the site on their own devices - Samsung, Dell Laptops, Self-built desktops and Apple products. 

#### ***HTML*** - https://validator.w3.org/nu/#textarea
* Code passes through without issues after adding alt titles to images. 
* Used "view page source" to get the pure HTML code of each page.  

![HTML validator](/documents/html%20validator.png)

#### ***CSS*** - https://jigsaw.w3.org/css-validator/
* Code passes through with no issues.

#### ***JavaScript and Python*** - https://jshint.com/  https://www.pythonchecker.com/
* I also passed the code through a jshint and PEP8 with no issues. 

#### ***Lighthouse Score***
* I passed the website through Google's Lighthouse to test accessibility and performance

![Lighthouse Score](/documents/lighthouse-scores.png)

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
1. From the bottom of the deploy page select your preferred deployment type by following one of the below steps:  
   * Clicking “Enable Automatic Deploys" for automatic deployment when you push updates to GitHub.
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.

# Credits
## ***General references:***
* Whilst I did try to deviate as much as possible, this project was influenced by the CI code project which I built before starting this project.
* Figma was used to create the wireframes.
* The site was developed using Gitpod.
* GitHub was used to store my repository.
* [Article Epics and how to make them](https://www.atlassian.com/agile/project-management/epics#:~:text=Epics%20are%20an%20important%20practice,of%20customers%20or%20end%2Dusers.)
* [coolers.co](https://coolors.co/603f3f-a0acca-e4b67c-de9f13-000000) was used to generate color scheme.
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* Recipe content was myself, BBC Goodfoods and Feasting At Home.
* Images:
  * Recipe images taken from [upsplash.com](https://unsplash.com) 
  * Background image and recipe default image designed by me in Canva.
* For this project I researched lots of other Django projects. Through other tutorials, I learned more about how to properly utilise all of Django's capabilities. Some code in this project has been inspired by these walkthroughs, although significant changes have been made to ensure that the code works with and for this specific Django App. Here is a comprehensive list of YouTube Pages that helped this project come to life.
    * [@Codemycom](https://www.youtube.com/@Codemycom)
    * [@DigitalFox-tutorials](https://www.youtube.com/@DigitalFox-tutorials)
    * [@Pyplane](https://www.youtube.com/@Pyplane)
    * [@veryacademy](https://www.youtube.com/@veryacademy)
* General references:
    * [Stack Overflow](https://stackoverflow.com/)
    * [Code Institute Learning Platform](https://codeinstitute.net/)
    * [Django Documentation](https://docs.djangoproject.com/en/3.2/)
    * [Bootstrap Documentation](https://getbootstrap.com/)

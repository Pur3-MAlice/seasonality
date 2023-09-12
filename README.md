# **Season to Taste**
This website has been built as a digital cookbook. Where people can upload their own recipes, comment, favourite and rate other people's submissions (including the admin's). This website aims to target the lack of community and collaboration within recipe websites. User submission give user a level of control, whilst the admin is also in charge of making sure the community is staying safe. It also aims to tackle the preamble that comes before recipes on websites that people find annoying, even if it is good SEO.

As a notice here - this is the second version of this app I made. The first version had many errors and it was early on in the development project that creating a new repo at that point was the best option. Here is the link to the old repo, [Season-To-Taste](https://github.com/Pur3-MAlice/season-to-taste/tree/main) it has the same Kanban Board and also lots of commits that should be noted.

![Responsive screenshot showing site on different screen sizes]()

[Deployed site]()

# **Table Of Contents**
* [**Season-to-Taste**](#season-to-taste)
* [**Planning Phase**](#planning-phase)
    * [**Site Aims**](#site-aims)
    * [**User Stories**](#user-stories)
    * [**Research**](#research)
    * [**Skeleton**](#skeleton)
    * [**Surface**](#surface)
* [**Agile Development Process**](#agile-development-process)
* [**Future development**](#future-development)
* [**Features**](#features)
  * [**Site Navigation**](#site-navigation)
  * [**AllAuth Pages**](#allauth-pages)
  * [**Site Instructions**](#site-instructions)
  * [**Main Page Content**](#main-page-content)
  * [**Error pages**](#error-pages)
  * [**Warning Modals**](#warning-modals)
* [**Testing Phase**](#testing-phase)
* [**Deployment**](#deployment)
* [Credits](#credits)

# **Planning Phase**
## **Site Aims:**
The site aims to:
1. Create community minded website that can share, favourite, rate and create recipes to create their own digital cookbook.
1. Tell the user if they have made any errors whilst using the website and prompt them as such.
1. Give user a lot of control with creation of content. Whilst Admin approves and can remove content that goes against guidelines to promote the community spirit.

How Will This Be Achieved:
To achieve the above, the site will:
1. Create environment that focuses on sharing own ideas, thoughts whilst also ensuring community guidelines are stuck to.
1. User submission and editing of their own recipe submissions, their own favourite lists and own ratings.
1. Author ability to delete and edit their own recipes whenever they would like. Delete function has fail safes incase of mis-type.
1. User validation via error messages.

## **User Stories:**
As an **Admin** I can...
1. As a Site Admin I can Draft Recipes so that control websites content and when content will be added to the site.
1. As a Site Admin I can CRUD recipes and comments so that to control the site's content to be in line with community guidelines.
1. As a Site Admin I can Approve or Disapprove recipe submissions and recipe edits so that I can control the website content.
 
As a **Site User** I can...(Logged in:)
1. As a Site user I can change my ratings and unsaved recipes so that reflect how my preferences may change.
1. As a Site user I can get access to the community guidelines so that I can understand how to appropriately join in with the community and understand when my submission may be removed or disapproved from site addition.
1. As a site user I can Rate each recipe so that show which recipe I liked and disliked, involving self in website's community.
1. As a site user I can comment on recipes so that to join in with the community and make suggestions.
1. As a Site userI can save recipes to my own 'digital cook book' so that easily access all my favourite recipes.
1. As a Site User I can Search recipes on the site by tags, author, and ingredients so that I can find appropriate results for my needs.
1. As a Site User I can submit my own recipes to the admin so that approved recipes can be added to the site.

As a **Site User** I can...(Not logged in:)
1. As a Site User I can sign in/up so that I can access features non signed-in members can't.
1. As a Site user I can get access to the community guidelines so that I can understand how to appropriately join in with the community.
1. As a site user I can Rate each recipe so that show which recipe I liked and disliked, involving self in website's community.
1. As a Site User I can Search recipes on the site by tags, author, and ingredients so that I can find appropriate results for my needs.

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
On the completion of this project, thsi database, while it does differ in some areas, is pretty much how my datbase structure has gone. Which I am happy with. 
 
## **Surface**
### **Color scheme:**
I knew I wanted my main theme to be pink and mustard as they are very in vouge right now. So i used this article https://www.thespruce.com/complementary-colors-that-go-with-pink-5188287 and then used https://coolors.co/f1cacc-df8a70-e8ac33-5a6950-13322c to create my colour Palatte

The final list of colors used has been placed in the below to check contrast scores.

![Color Scheme](/documents/wireframes/color-scheme.png)

![Color Grid](/documents/wireframes/contrast-grid.png)

### **Typography**:
To find my fonts i used thsi website: https://www.elegantthemes.com/blog/design/best-google-fonts. I went with Playfair Display and Monserrat, for a modern playful feel that would give the website levity.

# **Building Process**
  Using a Kanban Board system. And Something similar to sprints. 

  When it came to actually putting my Database Schema into reality a few things changed. Such as Saved and Categories. Plus I figured out I would need to make a model purely for the rating system I wanted to put in place. MVP this could just be likes, but to differentiate from the base of this project (which was taken from Code Insitutes 'Django Blog App') I wanted to add in this rating system that would calculate a recipes' popularity. This would also be the building block of the carousels on the recipe search page. I plan to have 'Diet' and even 'Season' Caraousels on the recipe search page so that site users can easily see recipes, the rating system will determine which recipes show up on these carousels. Or So I Plan... (Famous last words of a coder).

# **Features**
## **Site Navigation**
### **Add/Update Recipe Forms**

![add recipe](/documents/features/add-recipe.png)

![update recipe](/documents/features/update-recipe.png)

As described in the testing below - more errors are tried and tested with these forms and the other forms on the website.

### **Navbar and Signin/Out Logout Pages**
#### ***Signed Out:***
![sign-out nav](/documents/features/signout-nav.png)
#### ***Signed In:***
![sign-in nav](/documents/features/signin-nav.png) 
### ***Sign In:***
![sign-in form](/documents/features/signout-nav.png)
#### ***Form Errors:***
![sign-in error](/documents/features/sign-inerror.png)
### ***Sign Up:***
![sign-up form](/documents/features/register.png) 

As described in the testing below - more errors are tried and tested with these forms and the other forms on the website.
#### ***Form Errors:***
![sign-up error](/documents/features/sign-uperror.png)

As described in the testing below - more errors are tried and tested with these forms and the other forms on the website.
### ***Sign Out:***
![Sign out page](/documents/features/signout.png)

# **Future development**
1. I think that the ability to like and reply to other comments in the future would be a good addition to the site based on its aims.
1. For the user to be able to develop more than one list of favourites, like playlists of recipes.
1. I would also like for the users to be able to report recipes and comments to admin, or have a way of getting in touch with admin for site regulation.
1. Chnage password and Delete Profile
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
1. **Intended Outcome** - Had to restart the project
    * ***Issue Found:*** 
        * Due to some database issues i could not migrate any chnages after I had done my first migration.
    * ***Solution Used:*** 
        * Restarted the project and used db.sqlite3 instead of my main postgres db
1. **Intended Outcome** - Splicing List in Django Templates
    * ***Issue Found:*** 
        * I wanted to only have three of my categories on the main page, but nothing I did worked.
    * ***Solution Used:*** 
        * Discovered I could splice in the django html templates.
1. **Intended Outcome** - Be able to search entire db for recipes and their FKs
    * ***Issue Found:*** 
        * I wanted to be able too not only search the content of the recipes in the search bar but also search if they were connected to the FK. Nothing I tried worked until FK Q seac.
    * ***Solution Used:*** 
        *   FK Q Search
1. **Intended Outcome** - Star rating system not working. 
    * ***Issue Found:*** 
        * The avg of the recipe page would be affected. But the user input of the stars themselves would not hold the data.
    * ***Solution Used:*** 
        *  Used Javascript local storage to hold the browsers star rating instead.
1. **Intended Outcome** - Users be able to delete comments when user
    * ***Issue Found:*** 
        * Kept getting comment.id errors when refreshing page or clicking on new recipe page.
    * ***Solution Used:*** 
        * Removed this feature as it wasn't a requirement to have user delete comments.

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
1. Click the button labelled "Reveal Config Vars" and enter port / 8000. Click the "add" button.
1. Scroll to the top of the settings page, and nav to the "Deploy" tab.
1. From the deploy tab select Github as the deployment method.
1. Confirm you want to connect to GitHub.
1. Search for the repo and click the connect button.
1. From the bottom of the deploy page select your preferred deployment type by follow one of the below steps:  
   * Clicking “Enable Automatic Deploys" for automatic deployment when you push updates to Github.
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.

# Credits
* General references:
* For Django Models resources I used [Geeks For Geeks: Django Model](https://www.geeksforgeeks.org/django-models/?ref=lbp) https://docs.djangoproject.com/en/4.2/topics/db/models/
* Whilst I did try to deviate as much as possible, this project was influenced by the CI code project which I built before starting this project.
* For this project I researched lots of other Django projects. Through other tutorials I learned more about how to properly utlise all of Django's capabilities. Some code in this project has been inspired by these walkthroughs, although significant changes have been made to ensure that the code works with and for this specific Django App. Here is a comprehensive list of YouTube Pages that helped this project come to life : https://www.youtube.com/@Codemycom, https://www.youtube.com/@DigitalFox-tutorials, https://www.youtube.com/@Pyplane, https://www.youtube.com/@veryacademy
   
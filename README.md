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
    * [**Structure**](#structure)
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
* [**Technologies used**](#technologies-used)
* [Credits](#credits)

# **Planning Phase**
## **Strategy** 
### **Site Aims:**
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

## ***User Stories:***
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



### **Research:**
One of the first things I did when building the plan for this website was research. I wanted my website, not only to be useable and have a solid logic base but for it also to look modern and inviting. So part of my Planning Phase was not only wireframing, building a logic flow chart and a database schema. But also looking at websites with similar aims, and discussing with friends and family how they use recipe websites. What do they like, what do they dislike, and how can I emulate the good parts whilst removing the annoyance?  
Here are some of the sites I used for inspiration for the design of Season To Taste:
* Epics to User Stories to Tasks
* [thehappyfoodie](https://thehappyfoodie.co.uk/)
* [cookbookmanager](https://cookbookmanager.com/pricing)
* [Resturant Website Templates from Wix](https://www.wix.com/website/templates/html/restaurants-food)
  
  
  
## **Structure**   
To help me visualize a typical user journey around the site, I used [draw.io](https://app.diagrams.net/) to help me plan out the various routes a user could take through the site. This flow changed slightly throughout development. However, in general, it guided the process.
  
![User Journeys flow chart]()

# **Planning Phase:**

## **Skeleton**
### **Wireframes:**
* [Homepage wireframes]()  
* [OTHER PAGE WIREFRAME ETC]()


### **Database Schema**
Below is my initial database schema to map out the relations between users, recipes, comments and categories (also known as tags). This is a rough idea of what the database will look like in general, but at this point in the planning phase, I understand that this is subject to change. So I will also be showing a representation of the Database here once the project is ready for deployment.
![Color grid]()
 
## **Surface**
### **Color scheme:**

I knew I wanted my main theme to be pink and mustard as they are very in vouge right now. So i used this article https://www.thespruce.com/complementary-colors-that-go-with-pink-5188287 and then used https://coolors.co/f1cacc-df8a70-e8ac33-5a6950-13322c to create my colour Palatte
The final list of colors used has been placed in the below [color grid]() to check contrast scores.

![Color gird]()

### **Typography**:
Designers should avoid pure black typography — but which dark gray should we use?
https://medium.com/@TamerOkail/designers-should-avoid-pure-black-typography-but-which-dark-gray-should-we-use-2d7faa07083a

# **Building Process**
  Using a Kanban Board system. And Something similar to sprints. 

  When it came to actually putting my Database Schema into reality a few things changed. Such as Saved and Categories. Plus I figured out I would need to make a model purely for the rating system I wanted to put in place. MVP this could just be likes, but to differentiate from the base of this project (which was taken from Code Insitutes 'Django Blog App') I wanted to add in this rating system that would calculate a recipes' popularity. This would also be the building block of the carousels on the recipe search page. I plan to have 'Diet' and even 'Season' Caraousels on the recipe search page so that site users can easily see recipes, the rating system will determine which recipes show up on these carousels. Or So I Plan... (Famous last words of a coder).

  
# **Features**
## **Site Navigation**
### **Navbar**
#### ***Logo:***

![Site Logo]()
  
#### ***Signed Out:***
#### ***Signed In:***
#### ***Hamburger menu on smaller screen sizes:***
To display the menu properly on smaller screen sizes, a burger menu was implemented using bootstrap.  
### **Hero Images:**
I picked the hero images to portray the page's theme to the user. 
## **AllAuth Pages**
### ***Sign In:***
![sign-in form]()
#### ***Form Errors:***
![Invalid log in credentials]()
### ***Sign Up:***
![sign-up form]()
#### ***Form Errors:***
![Form errors for sign up form]()
### ***Sign Out:***
![Sign out page]()

# **Future development**

# **Testing Phase**
### ***Manual Testing:***
During the development process, I was manually testing in the following ways:-
*
### ***Bugs and Fixes:***
Below is a list of bugs I found during the development process. A lot of the bugs and fixes where minor enough that they were caught and easily amended by just seeing the redlines in gitpod. But here are a few that stumped me enough to write them down.
1. **Intended Outcome** - Had to restart the project
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        * 
1. **Intended Outcome** - Category Model for Diet and Season Broke my brain
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        *    
1. **Intended Outcome** - Duplicate in database
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        *   
1. **Intended Outcome** - Splicing List in Django Templates
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        *   
1. **Intended Outcome** - FK Q Search
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        *   
1. **Intended Outcome** - Main BG not filling page
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        *  
1. **Intended Outcome** - Stars not working 
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        *  
1. **Intended Outcome** - Comment Delete ?
    * ***Issue Found:*** 
        * 
    * ***Solution Used:*** 
        *                                                                

# **Deployment**

# **Technologies used**

# Credits

* General references:
* For Django Models resources I used [Geeks For Geeks: Django Model](https://www.geeksforgeeks.org/django-models/?ref=lbp) https://docs.djangoproject.com/en/4.2/topics/db/models/
* For this project I researched lots of other Django projects. Through other tutorials I learned more about how to properly utlise all of Django's capabilities. Some code in this project has been inspired by these walkthroughs, although significant changes have been made to ensure that the code works with and for this specific Django App. Here is a comprehensive list of YouTube Pages that helped this project come to life : https://www.youtube.com/@Codemycom, https://www.youtube.com/@DigitalFox-tutorials, https://www.youtube.com/@Pyplane, https://www.youtube.com/@veryacademy
   
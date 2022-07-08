# **Testing**

## **Manual Testing**
---
### **Features**
---
As part of my manual testing, I have tested that all of my features work as expected. Making sure to go through them across all different user types and various screen sizes and devices.

| ID | Test Case | Expected Output |
|---|---|---|
| 1 | Responsive Nav Bar - Full Screen and Mobile | All links have correct hover animation <br> On smaller devices navbar becomes single button drop down <br> All links navigate correctly across various account types |
| 2 | Footer | All links have correct animation <br> All links navigate to correct pages |
| 3 | Search Bar | Search bar returns response for if part or all of a recipe title is entered <br> Search returns response if a particular phrase in the ingredient field is entered <br> Search returns all recipes related to a topic if a topic is entered |
| 4 | Browse Buttons | 'All' button clears the query and returns all recipes <br> Clicking a topic returns all recipes associated with that topic |
| 5 | Pagination | Pagination buttons all function correctly <br> Pagination is still applied when browsing or searching and when moving to the next page the list remains filtered |
| 6 | Recipe Cards | Recipe cards show correct information <br> Link to the correct recipe <br> Display edit and delete buttons only to the author <br> Display time as hr and min correctly |
| 7 | Recipe Page | Displays correct recipe info <br> Like button works for users and redirects non authenticated users <br> Times are calculated and displayed correctly as hr and min <br> Edit and Delete buttons are visible only to the recipe author <br> Information is displayed neatly across various device sizes with none, small and large ammounts of information entered <br> User is able to comment if logged in <br> Guest is directed to log in <br> Users cannot use the submit button multiple times <br> Correct comment creator information is displayed <br> Only comment creators can see edit and delete buttons |
| 8 | Create Recipe | Title must be unique <br> Time and Nutrition fields must be positive integer <br> A topic and an allergy field must be selected <br> Image field uploads to cloudinary database <br> Difficulty is a selection of 3 options <br> Intro, Method and Ingredients are CKEditor fields and work correctly <br> Submit button can only be clicked once until processed <br> Form errors are displayed clearly to the user |
| 9 | Delete | User is informed of what they are about to delete <br> Only the correct user is able to delete a recipe or comment <br> User is redirected back if clicking the cancel button <br> Delete method functions correctly and cascades all relations |
| 10 | Profile | Displays correct users avatar and bio <br> Displays placeholder information if blank <br> Only shows update link for the correct user <br> Displays a recipe grid containing only the correct users submitted recipes <br> All features as with the home page recipe grid function correctly |
| 11 | Update Profile | Only the correct user has access to the page <br> Form is processed correctly <br> Image field uploads to cloudinary <br> Bio field character limit is set |

### **User Stories**
---
I have also gone over the user stories that I implemented and approached them from a user standpoint to judge if I was happy with the end result.

| ID | Test Case | Result |
|---|---|---|
| 1 | View Recipes | ✓ |
| 2 | Filter By Topic | ✓ |
| 3 | Search | ✓ |
| 4 | See comments and Likes | ✓ |
| 5 | Leave comments and Likes | ✓ |
| 6 | Remove comments and Likes | ✓ |
| 6 | See a users Profile | ✓ |
| 7 | Update Profile | ✓ |
| 8 | Create, Edit and Delete a Recipe | ✓ |
| 9 | All information is clear and easy to read | ✓ |

### **User Feedback**
---
I also asked my peers for their reviews on the website and made changes accordingly.

Some of the feedback that I implemented:
- The account button in the nav bar looked odd being a different shade to the other two nav buttons.
- The search icon was a little small.
- A message should be displayed if a search returns nothing.
- Navbar was a bit in the way when reading recipe instructions on smaller devices.

<br>

### **Responsive Design**
---
After researching the most commonly used screen resolutions ([Screen Resolutions Research Link](https://www.browserstack.com/guide/responsive-design-breakpoints)), I tested the responsive design on all the pages in this project at the resolutions widths of:

![Resolutions Image](/readme/assets/resolutions.jpg)

As they are the very common resolutions. I carried out the tests using a combination of the [Browser Stack Responsive Design Tester](https://www.browserstack.com/responsive), [Media Genesis RESPONSIVE WEB DESIGN CHECKER](https://responsivedesignchecker.com/) and [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/). 

<br>

### **Browser Testing**
---
I manually tested the project on the Browsers Firefox (version 94), Chrome (version 96) and Edge (version 95).

<br>

## **Automated Testing**
---

I tested the Performance, Accessibility, Best Practices and SEO of the site using Lighthouse in Chrome Developer Tools.

I also wrote a small number of automated python tests to test my views, forms and models.
If you wish to run these tests, you will need to swap the databases by swapping the commented out Test database that uses sqlite3 with the postgres database.

    DATABASES = {
    'default': dj_database_url.parse(os.environ.get('HEROKU_POSTGRESQL_COPPER_URL'))
    }
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }

## **Validation**
___
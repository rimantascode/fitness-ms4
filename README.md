# Fitness World MS 4

 
This website is designded for the fitness and gym sociaty, the potentional customers are able to see the exercises plans and nutritions plans, at the same time are able to by single items to improve the qulity of exerces and results.

The idea was todesign the website with the functionality quickly implement new products and exercises plans, nutritions plans, so any owner could manage the products not being skilled in web aplication development.

Hosted on [Heroku](https://fiteness-world-ms4.herokuapp.com/)
Repository on [GitHub](https://github.com/rimantascode/fitness-ms4)

## License

The project is shared for use with the [GNU General Public License v3](https://github.com/Pattern-Projects/oireachtas-ifd-project/blob/master/LICENSE)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

# UX

![Responsive Views of Home Page](source/responsive.png)


## User Stories

User stories shaped my idea of how to create this project. 

- Owner Goals.
- As admin I want to sell the exercises plans, nutrition Plans, nutrition and exercises products to earn money.
- As a admin I want the customers to register, so that I could keep the customers informed about the latest products.
- As admin I want to send emails about the latest products, so that will ensure returning customers.
- As admin I want the customers to register, so they would no loose the cart content.
- As  admin I want the user to register, so they would only this way would be able access the subscription content.
- As admin I want to add, edit, update, delete the products with the simple form. 


- User Goals
- As a user I can see my purchased products in my profile, so I can keep track for my own records.
- As a user I want to see the ratings of the products , that would helps to choose the product. 
- As a user I can sort the products by the ratings or price.
- As a user I want to buy single products, I need for the exercises.
- As a user I user I want to have the subscription, so that would let me to full content of the site.
- As a user I want can see the product in detail, so that provides more information about the product.


## Design Process

1. **Strategy plane:** There are a  lot of recipes websites, but I wanted to create my own app which would be not overloaded with information, and have a unique design. This project is B2C. Plus that was a good opportunity to get more familiar with the flask micro-framework. 
2. **Scope plane:** When I run through all ideas and user stories I began to realize how the website should look and how the recipes would have to be displayed for the users. It has to have a navigation bar at the top and which would have mobile responsive. The big picture in the main page and also the big picture when the recipe will be seen in detail. The recipes would be displayed in the format of the cards, with sensitive information, such as how long would it take to cook and how difficult it is, what the ingredients will the user need in order to cook. And the buttons with add, edit, and delete functions. The footer with the links to the social media about as and contact us form. I added a few more features at the end of the project such as pagination and how old is the recipe in order to keep the newest visible first. 
3. **Structure plane:** So when the decision was made of what features I will need, started to group the features. The user will land on the main page or in one of the categories. Decided to have a header in which would be navigation with the categories, the picture area on the main page. The main picture with a lot of dishes on the table. Add button and share links beneath. This part would stay the same all the time. Once clicked on of the categories the information from MongoDB would be pulled out and displayed in the cards with appropriate information. In the cards, they would be able to go to add, edit, or dish pages. This type of design is very easy to navigate no more than three clicks to reach the destination, and it easy learnable.
4. **Skeleton plane:** Once the structure plane was in place started to put all together using Figma. Added 5 categories of the main ingredients. The user can get the results only related to the category - the main ingredient. Add button takes the user to the add recipe page which consists of the header and a form, once filled up and meats all requirements can be submitted. When the visitor clicks on the categories the cards appear( as you can see in the mock-up I changed the size of the cards and how is the picture displayed). The user can see the picture on the left side of the card and the information on the right side. The name of the recipe, the cooking time, and the difficulty level is displayed and the majority of the ingredients required are also displayed. Down below three buttons delete, edit, and see the recipe in detail. The Edit page will keep the same structure - the navigation, hero image add button, and share links In place, but beneath there is a form that can be edited and the button update recipe. Once the button clicked the user will be taken to the dish.html page to review the changes. In the dish page there is a floating button with delete, edit, and add recipe functions to let the user do with the recipe what he wants straightway. 
5. **Surface plane:** When the skeleton plane was in place. Decided to do a research on what colors can make the people hungry? There were a lot of opinions, so narrowed down too much the colors. From Google fonts choice the fonts and finished the design. the footer took from materializecss and made the same color as navigation. 

## color Scheme

- ![#000000](https://placehold.it/15/000000/000000?text=+) `black`


- ![#008464 ](https://placehold.it/15/d40000/000000?text=+) `#d40000`
- ![#008464 ](https://placehold.it/15/ffc107/000000?text=+) `#ffc107 bootstrap warning`
- ![#008464 ](https://placehold.it/15/000F9A/000000?text=+) `#000F9A`
- ![#008464 ](https://placehold.it/15/dc3545/000000?text=+) `#dc3545 bootsrap danger`
- ![#008464 ](https://placehold.it/15/dc3545/000000?text=+) `#dc3545 bootsrap danger`

- ![#008464 ](https://placehold.it/15/6452d2/000000?text=+) `#6452d2`
- ![#008464 ](https://placehold.it/15/0dcaf0/000000?text=+) `#0dcaf0 bootsrap info`
- ![#008464 ](https://placehold.it/15/0dcaf0/000000?text=+) `#0dcaf0 bootsrap info`
- ![#008464 ](https://placehold.it/15/6c757d/000000?text=+) `#6c757d`

## Typography

sans-serif.

### Mockup

The website is a little bit different than in the mockup. Does not contain the about us and contact us pages as it is very simple, and the structure remained the same except the form and a text.

- [Mockup](https://www.figma.com/file/qRXUafOtVvw52gEOa81RPL/Untitled?node-id=0%3A1)

## Features

Features planned, implemented, and outlined for later development.

### Planned Features

- Documentation - ReadMe File, Licence & Mockups.
- Colour Scheme.
- Login mechanism
- Responsive design - Mobile First.
- Authentication.
- Logo.
- UX elements.
- Git - Version Control System
- GitHub - Remote Repository
- Hosted - on Heroku
- Deployed - On Github. 
- Subscription - using stripe
- cart for merchendise items.
- Take payments - using stripe.
- The emails sent on purchase of any merchendise item.
- The confirmation letters sent once the customer register.
- Subscribed user access only the exersises plans.
- Nutrition plans, not logged in user would be able to see 10 plans.
- Sell the items on the website realated to fitness.
- Implement the form to on front end to add the products to the website.
- Implement the quick way to add exercises plans using backend.
- Sort the products by categaries, price alhabeticly.
- Search the product in the store.
- in the home page the customer would be able to see the most popular and newst items.
- checkout form validation.
- Messages displaying on the top of the page, telling what actions is doing the website. for example when user loggs in it tells to the user that he is logged in. 
- Footer.
- News letter




### Existing Features

- Documentation - ReadMe File, Licence & Mockups.
- Colour Scheme.
- Login mechanism
- Responsive design - Mobile First.
- Authentication.
- Logo.
- UX elements.
- Git - Version Control System.
- GitHub - Remote Repository.
- Hosted - on Heroku.
- Deployed - On Github. 
- Subscription - using stripe.
- cart for merchendise items.
- Take payments - using stripe.
- The emails sent on purchase of any merchendise item.
- The confirmation letters sent once the customer register.
- Subscribed user access only the exersises plans.
- Sell the items on the website realated to fitness.
- Implement the form to on front end to add the products to the website.
- Implement the quick way to add exercises plans using backend.
- Sort the products by categaries, price alhabeticly.
- Search the product in the store.
- Checkout form validation.
- Messages displaying on the top of the page, telling what actions is doing the website. for example when user loggs in it tells to the user that he is logged in. 

### Features Left to Implement/fix

- Nutrition plans, not logged in user would be able to see 10 plans.
- In the home page the customer would be able to see the most popular and newst items.
- Footer.
- News letter


## Technologies Used.

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - **HTML** for strucutre
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - **CSS** for Styling
- [JavaScript](https://simple.wikipedia.org/wiki/JavaScript)
  - **JS** for creating dynamic functions, manipulating google places api.
- [jQuery](https://en.wikipedia.org/wiki/JQuery)
  - **jQuery** very usefull for traversing and events handeling
- [Google Chrome](https://www.google.com/chrome/)
  - Used for browsing and dev tools
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new)
  - Used for browsing and testing responsiveness.
- [Google](https://www.google.com/)
  - **Google** was used for research, work and testing responsiveness
- [Gitpod](https://www.gitpod.io/)
  - **Git** used for Version Control
- [GitHub](https://github.com/)
  - Repository hosted on **GitHub**
- [Heroku](https://dashboard.heroku.com/apps)
  - Website hosted on **Github Pages**
- [Am I Responsive](http://ami.responsivedesign.is)
  - Testing responsiveness of the website **Am I Responsive**
- [AWS](https://aws.amazon.com/)
  - Used to store the static files, and media.
- [fontawsome](https://fontawesome.com/)
  - Used icons
- [bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - Used icons
- [Figma](https://www.figma.com/)
  - used to make a mockup
- All the libraries including the flask micro Framework have to be installed. All of them are listed in the requirements.txt, how to install please see the **Deployment** section.


## Manual Testing

In this section will be provided the testing proccess and results. Because this project consists from multible apps, the each paragraph represent the appropriate app.

### cart 

the JS code was tested using JSHint, no major error. The functionality - update the quantity and remove the products from the cart. If you will use the arrows it will increase or decrease the amount and the links upadate and remove work and also the buttons KEEP SHOPPING and SECURE CHECKOUT takes to the appropriate destination. 
- [update-remove](source/update-remove.png)
views and context tested and with [http://pep8online.com/](http://pep8online.com/) no errors found.
the HTML was tested width [https://validator.w3.org/](https://validator.w3.org/) no errors found, except that it does not recognise jinja template language.


### checkout
views, webhook_handler, webbhooks, models, forms tested with:
[http://pep8online.com/](http://pep8online.com/) - no major probelms found except some lines are slightly to long.

The html files in templates forlder tested with:
[https://validator.w3.org/](https://validator.w3.org/) - 
no major problems found except that jinja templating couses and error.

stripe_elements.js tested with:
[https://jshint.com/](https://jshint.com/) - no major found just 2 warnings "'template literal syntax' is only available in ES6 (use 'esversion: 6')."

Testing form validation:
[form-validation](source/form-validation.jpg)

The checkout:
[form-before-submition](source/form-before-submition.png)
[stripe-webhook](source/stripe-webhook.png)
[email-confirmation](source/email.png)

### home

index html tested with:
- [https://validator.w3.org/](https://validator.w3.org/) - no major problems found, except that it does not understand jinja templating.

view tested width:
- [http://pep8online.com/](http://pep8online.com/)  - no major problems found. 

### products 
forms, models, views, admin validated with:

- [http://pep8online.com/](http://pep8online.com/) - no major problems except some lines are slightly to long.

the tempaltes tested with
- [https://validator.w3.org/](https://validator.w3.org/) - no major problems except jinja tempating is not recognized.

JavaScript tested with:
- [https://jshint.com/](https://jshint.com/) no majar problems found.

Manully tested the functionality. Products are dsplayed and can be arranged by Price and reating using the top navigation or the select box. All buttons work. edit and delete buttons can be seen only by the admin. 

- [edit-delete-products](source/edit-delete-products.png)
- [edit-delete-product-details](source/edit-delete-products.png)

- [no-buttons](source/no-buttons.png)
- [no-buttons-2](source/no-buttons-2.png)

### profiles

forms, models, views tested with:
- [http://pep8online.com/](http://pep8online.com/) - no major problems found.

the tempaltes tested with
- [https://validator.w3.org/](https://validator.w3.org/) - no major problems except jinja templating is not recognized.

JavaScript tested with:
- [https://jshint.com/](https://jshint.com/) no majar problems found.

The functionality tested manually, it works and updates the information.

### subscription_plans 

admin, models, views tested with:
- [http://pep8online.com/](http://pep8online.com/) - no major problems found, except some line are slightly too long.

The html files in templates forlder tested with:
[https://validator.w3.org/](https://validator.w3.org/) - 
no major problems found except that jinja templating couses and error.

### base.html 

base html validate not major error found. bases.html included to navigations one for bigger screen and other for smaller screens.
### CSS Validation

To validate my CSS and HTML code I used [https://validator.w3.org/](https://validator.w3.org/) 




### Testing on Browsers

Tested on Google Chrome, Opera, Mozilla firefox. No issues.

### Testing on Devices

Used Google Chrome, Opera, Mozilla Firefox browser to test the responsiveness, for all sizes looks satisfing, but on Galxy fold does not look, it has to be looked in to it.

## Deployment

The process involved:

- In this project, you have to use Code institute template [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Click the green button "use this template" 
- How to create a new repository [here](https://docs.github.com/en/enterprise/2.15/user/articles/create-a-repo) , but in this case enter the title of the project, the description, choose privet or poblic, and click create repository from template. 
- On the GitHub repository settings page move to GitHub Pages section
- Change source to master branch. (Or any desired branch)

- Once the workspace is ready:
- In the terminal, in your root directory
- Type 'git clone ' followed by the code taken from the GitHub repository
- `https://github.com/rimantascode/MS3-cookbook.git`
- for example `git clone https://github.com/rimantascode/MS3-cookbook.git`
- Select all files and move out of the folder MS3-cookbook into the root directory. 
- Install requirements.txt by typing in the terminal 
- `pip3 install -r requirements.txt`

- create the database in [mongoDB](https://www.mongodb.com/) as it shown in the picture. cook_book is a database, and categories, difficulty, prep_time, recipe are the collections.
- ![mongoDB structure](source/mongoDB.png)

- create an enviroment variable in gitpod settings,[gitod settings](https://gitpod.io/settings/)

- ![Environment Variable](source/MONGO_URI.jpg)
- value is equel:
mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
- Organization/Repository: is your GitHub **username**
- Also you need to create the **SECRET_KEY** environment variables value can be anything just do **not** do simple, like 1234 
- ![SECRET_KEY](source/SECRET_KEY.jpg)

#### IMPORT COLLECTIONS INTO mongoDB

- Now we need to import the data into the collections.
- Type in the terminal

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection categories --type json --file categories.json`

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection difficulty --type json --file difficulty.json`

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection prep_time --type json --file prep_time.json`

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection recipe --type json --file recipes.json`

- Type in the terminal
- `python3 app.py`
- click on the blue button to open in the browser.
- It is ready to use. 

- Feel free to make any changes to it.
- Your website with any made changes will appear.
- Saved changes in gitpod and to the website will appear after refreshing the page.


## Deploy to Heroku

- You have to create a new app in [Heroku](https://dashboard.heroku.com/new-app)
- give a unique name and choose a region to Europe.
- a gave the name of the app "testing-deploymenta" for testing porpuse.
- Click on Settings, and then the button "Reveal Config Vars".
- Enter MONGU_URI with the value you used to create environment variable.
- Enter SECRET_key with value you used to create environment variable.
- PORT value is 5000.
- IP value is 0.0.0.0.
- in the terminal
- `heroku login -i` , and enter the credentials.
- In the terminal, go to deploy section you will see the line similar to this.
- `heroku git:remote -a testing-deploymenta`
- create requirements.txt
- `pip3 freeze > requirements.txt`
- create Prockfile with a capital "P" this is a requirement.
- ` echo web: python app.py > Procfile`- and then `git add . ` and `git commit -m"added requirements.txt and Prock files" `
- `git push heroku master`
- once it has been pushed, in the terminal.
- `heroku ps:scale web=1`
- ready to use.
- ` heroku open`


## Credits
- Thank you.
- [Waitrose.com](https://www.waitrose.com/content/waitrose/en/home/recipes/recipe_directory/b/breaded_chicken_andwatercresssalad.html#_) - used the recipes, and the pictures for learnign and demonstrative porposes only. Once the project will be assested all data will be deleted.

- Thank you.
- [css tricks](https://css-tricks.com/line-clampin/) for a piece of code made to look my text very nice faded out.
Thank you.
- [photo](https://www.flickr.com/photos/dennis/102679650
https://live.staticflickr.com/32/102679650_cd10235c8f_k_d.jpg) for very nice picture.)


### Acknowledgements

Thank you inspiration, very usefull guidence and tips:

- Seun Owonikoko @seun_mentor
- Code Institute
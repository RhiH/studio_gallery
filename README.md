![Studio_Gallery](media/wireframes/studio-gallery_responsive.png)


# Studio Gallery

Studio Gallery is a online store enabling the public to buy prints of artwork directly from the artists. They are able to search the site and see what art is currently available to purchase, and are able to purchase as many prints within certain limitations, paying with their card via Stripe functionality.

Users are also able to create a profile for faster purchasing and to see their previous orders.

## Table of Contents

- [UX](#ux)
- [Site User Goals](#site-user-goals)
- [Design Choices](#design-choices)
- [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
- [Future Goals](#future-goals)

- [Technology Used](#technology-used)

- [Testing](#testing)

- [Deployment](#deployment)

- [Credits](#credits)


## UX

**The Scenario**

Artists can find it difficult to have a regular income if they solely rely on large expensive pieces of work selling to a small audience who can afford to buy and have enough space to display works of art. 

In addition, if selling via a gallery, the gallery will take a commission – usually between 40 – 60% of the RRP of the piece, meaning an artist must consider this when pricing their work. This increases the overall cost of their piece, potentially shrinking their audience further.

If the artist has an agent for representation, they also tend to work on a commission basis and again, the artist must factor this in when pricing their work, although having a good agent can ensure the artist has new opportunities. 

Most artists who are not household names do not tend to be represented by galleries or agents, although they may show their work for a short term in a gallery space. Consequently, many artists must supplement their income with paid work, which can have an impact on the amount of time and energy available to create new pieces and promote their work to appeal to a wider audience.

**The Concept Solution**

Create a space online for artists to showcase their work directly to the public and enable the public to purchase print versions of the artists’ work.

Prints can be produced in different quantities, artists can choose to have them pre-printed prior to sales, as they may already have a stock of work ready to sell; or can choose to have an approach similar to print on demand with their preferred local print shop.

Prints can appeal to a wider market, who may not wish to invest in the original piece or who cannot afford to purchase one but would like to have a copy of the artwork they admire and also support the artist, much like the just a card initiative. (LINK)

A collective group of artists would appeal to a wider range of customers, rather than a single artist website, and costs of the site could be split across the group making it a cost effective way of being on a website without having to pay as much as if it was their own site, which would not receive as much traffic as a shared site.

Marketing costs could also be shared by the collective, and potentially the collective could work together to host real life events such as exhibitions, which they could use the website to drive footfall to the exhibition to increase sales, and also in a circular fashion, drive traffic to the website during the exhibition to increase sales and awareness of their collective work.

Whilst there are already a number of sites such as Etsy and Redbubble who showcase artists and provide a space for makers to sell their work directly, these are large sites and very often a consumer might say they bought it on Etsy, rather than the name of the artist or crafter who made the work in question. Within the selected group of artists on the site it would be easier to find a specific artist, rather than hunting across a much larger website with significantly more competition. 

**Target Audience Examples:**

Marsha and Chris, well-travelled early retirees who appreciate going away on a whim. The appreciate good wine, good books and good art. Marsha in particular loves sending things she finds beautiful to their wide circle of friends and has often recommended new and up-coming artists to her circle.

Katie – single, early thirties. She enjoys decorating her home with her own style, dislikes the current trend on colouring all spaces at home in grey. Likes unusual art and enjoys supporting artists when she can, does not have a large disposable income.

**Marketing:**

The main goal of the site is to assist artists to increase their income while reducing overheads associated with running a website where you can purchase products.

Having a shared site, allows the artists to promote themselves and each other, increasing the potential audience for their work, and as the site does not have a large number of artists, this improves the opportunities of the customer remembering the site and the artist name, meaning they are more likely to revisit in future and promote the site by word of mouth.

A Contact Us page ensures that the customer can communicate if needed with the artists, and the information about each artist, their practice and their pieces means the site has more interest than just a site which displays the work alone.

## Site User Goals

1. As a user I expect the site to be accesible
2. As a user I expect my purchases to be secure
3. As a user I expect the site to be responsive.

**Visitor Goals**

4.	As a visitor I want to be able to view all the art to see what’s available.
5.	As a visitor I want to be able to learn more about the artists and their work.
6.	As a visitor I want to be able to filter the work to see each artists' individual work.
7.	As a visitor I want to be able to sort the prints by price.

**Customer Goals**

8.	As a customer I want to be able to purchase more than one print of the same picture.
9.	As a customer I want to be able to have my own login.
10.	As a customer I want to be able to amend the items in my basket.
11.	As a customer I want to be able to remove items from my basket.
12.	As a customer I want to be able to pay by card.
13. As a customer I want to be able to use a contact page if I have a question.

**Artist Goals**

14.	As an artist I want to be able to display my work to the public and sell prints of it at a price I can set myself.
15.	As an artist I want to be able to have an account which enables me to log in.
16.	As an artist I want to be able to edit, create and delete work when I want to do so.

I created a user story list in terms of priority, with all the goals in numerical order and then sorted in terms of priority.

![Studio_Gallery](media/site_images/user_story_list.png)

Critical items were seen as essential, these are the secure purchasing, followed by accessible and responsive design. Card payments, superuser login, CRUD functionality, a contact page and the ability to see the prices of the products were listed as needed for the site. The ability to remove, amend and edit items in the basket, along with the option to see all products at were classed as wanted, and finally customer login, sort by price, filter by artist and a way to view information about the artist was seen as nice to have.

## Wireframes

Wireframes were used to create an idea of how the site should look on different devices.

![Studio_Gallery](media/wireframes/desktop_wireframe.png)
![Studio_Gallery](media/wireframes/product_desktop.png)
![Studio_Gallery](media/wireframes/tablet_wireframe.png)
![Studio_Gallery](media/wireframes/mobile_wireframe.png)

User stories: [2](#site-user-goals), [3](#site-user-goals)

## Site Design

**Design Choices**

It was decided to keep the project as simple as possible, given this was the first time Django had been used. Ensuring things were kept as simple as possible meant that the focus could remain on the site as a whole. As the site is to display art in most appealing way, vivid colours were not used as these could easily detract from the work, and put off the consumer. 

The colour scheme was kept simple, with sticking to a white background with black text. Grey text weas also used to give the site a slightly softer feeling.

![Studio_Gallery](media/site_images/colour_scheme.png)

Hex codes as follows: white: # ffffff, black: # 000000, grey: #555555

The site home page is colourful as it does not display any artist's work, but is a studio space. It was decided to have a colourful landing page as this was more enticing than having the artwork on the home page, and it meant that this could be a static image which could be updated when required, as opposed to featuring an image which might need to be changed at short notice if an artist no longer wished for their work to be displayed.

![Studio_Gallery](media/studio.jpg)

The image is of a working artist studio, hence it has equipment and supplies ready to use by the artist. Also gap in the wall close to the socket subtly shows the viewer that this is a place where creativity is allowed and the artist does not need to be too precious about their surroundings. This is not a posed image - this is a real studio.



![Studio_Gallery](media/site_images/logged_in_user_previous_order.png)
Logged in profile with saved address and previous order history.

![Studio_Gallery](media/site_images/order_success_page.png)
Notification success of adding items to basket.

![Studio_Gallery](media/site_images/profile_update_page.png)
Order confirmation information for logged in user.

![Studio_Gallery](media/site_images/checkout_page_not_logged_in.png)
Checkout option – not logged in.

![Studio_Gallery](media/site_images/update_shopping_bag.png)
Bag quantity is 3 items.

![Studio_Gallery](media/site_images/item_added_to_bag_message.png)

![Studio_Gallery](media/site_images/product_detail.png)
Viewing the art and selecting more than 1 item.

![Studio_Gallery](media/site_images/logged_in_superuser_edit_option.png)
Filtering products by artist, with biography text underneath artist friendly tag (surname) for logged in superuser.

![Studio_Gallery](media/site_images/product_management.png)
Adding product page with drop down list for selecting the artist for logged in superuser. 


![Studio_Gallery](media/site_images/verify_email_message.png)
Sign up verification notice – reminding new users to verify their email address.

![Studio_Gallery](media/site_images/register.png)
Creating a new account page. 

![Studio_Gallery](media/site_images/all_artists.png)
All artists page, with information about where the artist is from, and for some where they are currently based with tags to take the user to each artist’s filtered work.!

![Studio_Gallery](media/site_images/contact_us_page)
Contact us page for customers to send queries or comments about the site directly to the site admin.


![Studio_Gallery](media/site_images/artist_product_filter.png)
Filtering products by artist (not logged in).

![Studio_Gallery](media/site_images/product_sorted_price.png)
Sorting products by price (low to high), with user not logged in.


![Studio_Gallery](media/site_images/product_sorted_price_with_edit.png)

Products page for logged in superuser to edit and delete items. Currently there is only a login to access all items, a later adaptation will ensure that it is only specific superusers who can edit and delete their own work. This is an option for future improvements.




### Information Architecture

**Product Data**

| Title            | Key In Database | Form Validation      | Data Type   |
|------------------|-----------------|----------------------|-------------|
| Product ID       | SKU             | No Validation        | Primary Key |
| Product Name     | name            | max_length 254       | Charfield   |
| Product Category | category        | max_length 254       | Charfield   |
| Price            | price           | decimal places 2     | Decimalfield|
| Image            | image           | Null True, blank True| ImageField  |
| Description      | description     | max_length 1000      | Charfield   |

**Category Data**

This is currently an underutilised table - and will be updated as the site grows

| Title            | Key In Database | Form Validation      | Data Type   |
|------------------|-----------------|----------------------|-------------|
| Category ID      | name            | No Validation        | Primary Key |
| Friendly Name    | friendly_name   | max_length 254       | Charfield   |
| Identifier       | identifier      | max_length 5         | Charfield   |
| Biography        | biography       | max_length 1000      | Charfield   |

**Artist Data**

| Title            | Key In Database | Form Validation      | Data Type   |
|------------------|-----------------|----------------------|-------------|
| Category ID      | PK              | No Validation        | Primary Key |
| Name             | name            | max_length 254       | Charfield   |
| category         | category        | Null true, blank true| Foreign Key |
| Biography        | biography       | max_length 1000      | Charfield   |


**User Table**

|Title            |	Key In Database         |	Form Validation     |	Data Type     |
|-----------------|-------------------------|---------------------|---------------|
|Account ID       |	_id                     | No Validation       |	Primary Key   |
|First Name       |	first_name              |	max length 20       |	CharField     |
|Last Name        |	last_name               |	hashed min length 8 |	CharField     |
|E-mail Address   |	email                   |	Must contain @ etc	| Email         |
|Street Address   |	default_street_address1 |	max length 128      |	CharField     |
|Street Address 2 |	default_street_address2 |	max length 128      |	CharField     |
|City Or Town     |	default_city_town	max   | length 128          |	CharField     |
|County/State     |	default_county_state    |	max length 64       |	CharField     |
|Postal Code      |	default_postcode_zi     |	max length 12       |	CharField     |
|Contact Number   |	default_telephone_number|	Number max length 20|	CharField     |
|Country	        |country                  |	pycountry select    |	Option        |

**Orders Table**

|Title             |	Key In Database |	Form Validation     |	Data Type     |
|------------------|------------------|---------------------|---------------|          
|Order Number      |	order_number    |	No Validation       |	Primary Key   |         
|User Profile      |	user_profile    |	text                |	Foreign Key   |                 
|First Name        |	first_name      |	max length 100      |	CharField     |       
|Last Name         |	last_name       |	max length 100      |	CharField     |
|Email             |	email           |	max length 100      |	CharField     |
|telephone Number  |	telephone_number|	max length 20       |	CharField     |
|Street address 1  |	street_address1 |	max length 100      |	CharField     |
|Street address 2  |	street_address2 |	max length 100      |	CharField     |
|City Town         |	city_town       |	max length 100      |	CharField     |
|County/State      |	county_state    |	max length 100      |	CharField     |
|Postcode Zip      |	postcode_zip    |	max length 8	      | CharField     |
|Country           |	country         |	country select	    | Option        |
|Order Date        |	order_date      |	datetime.date.today |	DateField     |
|Total Order       |	total_order     |	max digits 10	      | DecimalField  |
|Delivery Charge   |	delivery_charge |	max digits 5        |	DecimalField  | 
|Grand total       |	grand_total     |	max digits 10       |	DecimalField  |





## Technology Used

* HTML
* CSS
* Javascript
* Python

## Tools

- [Fontawesome](https://fontawesome.com/icons)
- [Django](https://www.djangoproject.com/)
- [Am I Responsive](https://ui.dev/amiresponsive)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Chrome dev tools](https://developer.chrome.com/docs/devtools/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku](https://heroku.com)
- [AWS](https://aws.amazon.com/)
- [ElephantSQL](https://www.elephantsql.com/)


Validation:
- [WC3 Validator](https://validator.w3.org/)
- [JShint](https://jshint.com/)
- [Lighthouse](https://www.webpagetest.org/lighthouse)
- [Wave Validator](https://wave.webaim.org/)

## Testing

The project was tested during the process of creating it and errors were fixed along the way during the creation of the site, except for the Contact page which worked and then at a later point failed to work. As such it was decided to leave this and continue on with the overall functionality. Unfortunately this, some CSS elements which were not displaying correctly and more thorough testing did not go ahead after deployment due to time constraints.

---
* issue: url not linking correctly to contacts page
* cause: url not correctly formatted
* resolution: url updated, link working
---
* issue: artist page not generating properly
* cause: under investigation
* resolution: temporary 'all artists biographies' page created as holding page until issue is discovered and resolved
---
* issue: font is difficult to read on most pages
* cause: Lato slim chosen as font, combined with text-muted, creating text that is difficult to see
* resolution: text-muted replaced with text-black, Lato slim replaced with Lato regular
---
* issue: artist model not working
* cause: under investigation
* resolution: amendment to model not successful - ongoing
---
* contact page not sending emails
* cause: fault caused by line not removed for default setting for emails in settings.py
* resolution: settings.py updated - emails now successfully sending
---
* issue: artist model still not updating correctly
* cause: under investigation
* resolution: delete migrations and re migrate model. Not successful - ongoing
---
* issue: artist model still not updating correctly
* cause: under investigation
* resolution: temporary links added to temporary all artist biographies page to link to products while investigation is ongoing
---
* issue: artist model not updating correctly
* cause: under investigation - table not added correctly
* resolution: delete dbsqlite3 and remake all migrations. Not successful - followed steps to step back to previous commit
---
* issue: redeployment retains old database not current database
* cause: elephantsql retains original database
* resolution: create new instance, loaddata to new database, site deployed successfully
---
* issue: site failing at deployment after redeployment
* cause: answer found on stack overflow - backports info issue.
* resolution: add python_version<"3.9" to requirements.txt file
---
* issue: linking to products via all artist page not working on deployed site, but working on development site
* cause: observation showed that deployed site converts link whereas development site does not
* resolution: amend links to deployed site path for products filtering and note that dev site will not link correctly, but deployed site will.
---

A significant amount of time was spent trying to get the models in the artists app working. Despite various attempts at different solutions, ultimately it was decided to create links on the all artists page which would take the user to the products for each artist, and at a later date the artist_detail page (already created) would be utilised once the source of the exact issue is found and a solution created.

# Deployment

Deployment Requirements

This site was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was commited to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal. Django was used throughout the project. It is necessary to install Django to create the apps required to run the site. Nb python3 was the command used here, please choose the most appropriate for you.
```
Python3 
PIP package installer
Stripe Payment infrastructure
```
Deploying Locally

Clone a copy of the repository by clicking code at the top of the page and selecting 'Download Zip' when this has downloaded, extract the files to your folder of choice. Alternatively if you have git installed on your client you can run the following command from the terminal.

Open up your local IDE and open the working folder.

Ideally you will want to work within a virtual environment to allow all packages to be kept within the project, this can be installed using the following command (please note some IDE's require pip3 instead of pip, please check with the documentation for your chosen IDE)

Create a new folder within the root dir called env.py. Within this file add the following lines to set up the environmental variables.
import os
```
os.environ["SECRET_KEY"] = "[Your Secret Key]"
os.environ["DEV"] = "1"
os.environ["HOSTNAME"] = "0.0.0.0"
os.environ["STRIPE_PUBLIC_KEY"] = "[Your Stripe Key]"
os.environ["STRIPE_SECRET_KEY"] = "[Your Stripe Secret Key]"
os.environ["DATABASE_URL"] = "[Your DB URL]"
```
Database setup

To set up your database you will first need to run the following command. 
```
python3 manage.py migrate
```
To create a super user to allow you to access the admin panel run the following command in your terminal and complete the required information as prompted
```
python3 manage.py createsuperuser
```
From there you should now be able to run the server using the following command
```
python3 manage.py runserver
```
Next close the server in your terminal using ctrl+c (cmd+c on mac) and run the following commands to populate the database
```
python3 manage.py loaddata products/fixtures/categories.json
python3 manage.py loaddata products/fixtures/products.json
python3 manage.py loaddata artists/fixtures/artist_categories.json
```
For deployment the following will be required:
```
Elephant SQL
Heroku
AWS
```
Link Elephant SQL with Heroku project area. 

Set up AWS with necessary S3 bucket for static files, policy, group, user and link with appropriate keys to heroku.

Deploying to Heroku

To run this application in an online environment you will need to deploy the code to Heroku. Before moving on to this section please ensure you have followed the instructions for local deployment and this has been successfu

in the settings tab select Reveal Config Vars and copy the pre populated DATABASE_URL into your settings.py file in your project
in the Config Vars in Heroku you will need to populate with the following keys

Ensure all necessary keys - secret and public are stored in config vars on Heroku.

Key	Value
```
AWS_ACCESS_KEY_ID	[your value]
AWS_SECRET_ACCESS_KEY	[your value]
SECRET_KEY	[your value]
DATABASE_URL [your value]
DEFAULT_FROM_EMAIL [your value]
EMAIL_HOST_PASS [your value]
EMAIL_HOST_USER [your value]
STRIPE_PUBLIC_KEY	[your value]
STRIPE_SECRET_KEY	[your value]
STRIPE_WH_SECRET [your value]
USE_AWS	TRUE
```

Now this has been configured you will now migrate the local database to the cloud database using the migrate command as below
```
python3 manage.py migrate
```
Next you will need to create a super user and populate the database as described in the database set up section
When the migrations and data has been loaded, in your Heroku dashboard select the Deploy tab

From here select the Github option and connect the repository from GitHub and select the branch (Master) to deploy from.

It is advised to select automatic deployment to ensure for each push to Github the hosted version is up to date.

When it is deployed, you can launch the site via the link in Heroku.

# Future Goals

**Product growth options:

As the site currently only offers prints of artists' work, more options of the type of products could be available. This could vary between original pieces to canvas, textile and other products such as phone cases or notebooks could be printed with the art and shipped to the customer. This could be linked via services which already offer this business model, meaning the work could be sold globally and be created within the country/region to ensure shipping times and taxes would be kept to a minimum, whilst increasing the returns for the artists at a low cost.

**Site growth options:

In terms of what the site offers, increasing the number of artists, and artworks are the simplest way of growing the site.  Also improving search functionality to consider colour or theme as search options to increase the level of customer satisfaction. Adding in other options such as a sign up newsletter utilising a marketing automation platform such as Mailchimp, creating a featured artist of the month with an interview of the artist - perhaps including a short videoclip of them talking about their processes could help customer engagement. 

The site could offer artists stock management options, should artists wish to offer limited edition/one-off pieces, with higher costs. Different delivery options could also be offered as standard, especially for higher price point items, where insurance would be advisable. 


# Credits

**Media

Art images were sourced from [kaggle](https://www.kaggle.com/datasets "Link to Kaggle datasets")

Artist images were sourced from Google Images search.

Tyra Goodley https://www.artsyshark.com/2013/01/27/artists-at-work/
Andrew F https://natureinart.org.uk/artistinresidence/
Tom Werner https://www.liveabout.com/what-do-artists-do-1122810
Unnamed male artist by Unsplash https://www.shopify.com/blog/211990409-how-to-sell-art-online
Unnamed female artist by Gorodenkoff https://stock.adobe.com/images/talented-innovative-female-artist-draws-with-her-hands-on-the-large-canvas-using-fingers-she-creates-colorful-emotional-sensual-oil-painting-contemporary-painter-creating-abstract-modern-art/298117629
Unnamed Female standing in front of artwork 

All artist names, biographies, artwork names and descriptions are my own invention.

**Code 

This work was based on the Boutique Ado project by Code Institute, and references from 

Python
Django
Bootstrap


# Acknowledgements

A huge thank you to my mentor Richard without whom I would have not managed to submit anything. 

Communities on Slack and Stack Overflow were invaluable for assisting with technical problems. I consulted both regularly throughout the project.

A massive thank you to my colleagues, friends and family - who have cheered me on throughout my course. A special thanks to Hayley and Carrie for thoroughly testing my site.

All mistakes are very much my own.










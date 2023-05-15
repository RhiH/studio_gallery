![Studio_Gallery](media/wireframes/studio-gallery_responsive.png)


# Studio Gallery

Studio Gallery is a online store enabling the public to buy prints of artwork directly from the artists. They are able to search the site and see what art is currently available to purchase, and are able to purchase as many prints within certain limitations, paying with their card via Stripe functionality.

Users are also able to create a profile for faster purchasing and to see their previous orders.

## Table of Contents

- [Project Goals](#project-goals)
- [Artist Goals](#artist-goals)
- [Customer Goals](#customer-goals)
- [Site User Goals](#site-user-goals)
- [Design Choices](#design-choices)
- [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
- [Future Goals](#future-goals)

- [Technology Used](#technology-used)

- [Testing](#testing)

- [Deployment](#deployment)

- [Credits](#credits)

## Project Goals

The overall project goal is to ensure that consumers can easily purchase printed art direct from the artists themselves, cutting out the need for artists to involve third parties who would charge commission, sometimes as much as 60% of the overall price. The art needs to be displayed in a simple manner so as not to distract the customer when thinking of making a purchase.

**Artist Goals**

* As an artist I want to be able to display my work to the public and sell prints of it at a price I can set myself.
* As an artist I want to be able to sell affordable pieces to increase my revenue streams.
* As an artist I want to be able to create new income streams by displaying my work alongside other artists.
* As an artist I want to be able to set the prices to the RRP so I can have the full benefit of sales of my work rather than have any commission taken, other than running costs for the site itself, which I can share with other artists.
* As an artist I want to be able to have an account which enables me to log in, edit, create and delete work when I want to do so.
* As an artist I want to be able to control the numbers of prints I sell.

**Customer Goals**

* As a buyer I want to be able to view all the art at once.
* As a buyer I want to bw able to learn more about the artists and their work.
* As a buyer I want to be able to filter the work to see each artists' individual work.
* As a buyer I want to be able to sort the prints by price.
* As a buyer I want to be able to login to make repeat purchases.
* As a buyer I want to be able to see my previous purchases in my account.
* As a buyer I want to be able to update my details in my account.
* As a buyer I want to be able to make a purchase without logging in.
* As a buyer I want to be able to purchase more than one print of the same picture.
* As a buyer I want to be able to buy art at affordable prices.
* As a buyer I want to be able to support the artists directly.
* As a buyer I want to be able to amend the items in my basket.
* As a buyer I want to be able to remove items from my basket.

**Site User Goals**

* To be able to view art and purchase prints of the art and have confirmation of my order sent to me.
* To be able to amend the quantities of my basket prior to checkout.
* To be able to view an individual's art on the same page.
* To be able to purchase multiple prints and get free delivery.
* To have my info saved so I can make easier purchases and look up past purchases.

## Design Choices

It was decided to keep the project as simple as possible, given this was the first time Django had been used. Ensuring things were kept as simple as possible meant that the focus could remain on the site as a whole. As the site is to display art in most appealing way, vivid colours were not used as these could easily detract from the work, and put off the consumer.

## Wireframes

Wireframes were used to create an idea of how the site should look on different devices.

![Studio_Gallery](media/wireframes/desktop_wireframe.png)
![Studio_Gallery](media/wireframes/product_desktop.png)
![Studio_Gallery](media/wireframes/tablet_wireframe.png)
![Studio_Gallery](media/wireframes/mobile_wireframe.png)

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




## Future Goals

**Product growth options:

As the site currently only offers prints of artists' work, more options of the type of products could be available. This could vary between original pieces to canvas, textile and other products such as phone cases or notebooks could be printed with the art and shipped to the customer. This could be linked via services which already offer this business model, meaning the work could be sold globally and be created within the country/region to ensure shipping times and taxes would be kept to a minimum, whilst increasing the returns for the artists at a low cost.

**Site growth options:

In terms of what the site offers, increasing the number of artists, and artworks are the simplest way of growing the site.  Also improving search functionality to consider colour or theme as search options to increase the level of customer satisfaction. Adding in other options such as a sign up newsletter utilising a marketing automation platform such as Mailchimp, creating a featured artist of the month with an interview of the artist - perhaps including a short videoclip of them talking about their processes could help customer engagement. 

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


# Credits

This work was based on the Boutique Ado project by Code Institute, without which this project would not have gotten as far as it did.

A huge thank you to my mentor Richard without whom I would have not managed to submit anything. 

Communities on Slack, Stack Overflow and various other websites - too many to recall without whom I would have failed to get anything working at various points.

All mistakes are very much my own.










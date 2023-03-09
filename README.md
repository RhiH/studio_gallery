![Studio_Gallery](media/wireframes/studio-gallery_responsive.png)


# Studio Gallery

### Studio Gallery is a online store enabling the public to buy prints of artwork directly from the artists. They are able to search the site and see what art is currently available to purchase, and are able to purchase as many prints within certain limitations, paying with their card via Stripe functionality.

### Users are also able to create a profile for faster purchasing and to see their previous orders.

## Table of Contents

- [Project Goals](#project-goals)
- [Artist Goals](#artist-goals)
- [Customer Goals](#customer-goals)
- [Site User Goals](#site-user-goals)
- [Design Choices](#design-choices)
- [Wireframes](#wireframes)
- [Future Goals](#future-goals)

- [Technology Used](#technology-used)

- [Testing](#testing)

- [Deployment](#deployment)

- [Credits](#credits)

## Project Goals

The overall project goal is to ensure that consumers can easily purchase printed art direct from the artists themselves, cutting out the need for artists to involve third parties who would charge commission. The art needs to be displayed in a simple manner so as not to distract the customer when thinking of making a purchase.

**Artist Goals**

* As an artist I want to be able to display my work to the public and sell prints of it at a price I can set myself.
* To sell affordable pieces to increase my revenue streams.
* As an artist I want to be able to create new income streams by displaying my work alongside other artists.
* As an artist I want to be able to set the prices to the RRP so I can have the full benefit of sales of my work rather than have any comission taken, other than running costs for the site itself, which I can share with other artists.
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

To be able to view art and purchase prints of the art and have confirmation of my order sent to me.
To be able to amend the quantities of my basket prior to checkout.
To be able to view an individual's art on the same page.
To be able to purchase multiple prints and get free delivery.
To have my info saved so I can make easier purchases and look up past purchases.

## Design Choices

It was decided to keep the project as simple as possible, given this was the first time Django had been used. Ensuring things were kept as simple as possible meant that the focus could remain on the site as a whole. As the site is to display art in most appealing way, vivd colours were not used as these could easily detract from the work, and put off the consumer.

## Wireframes

Wireframes were used to create an idea of how the site should look on different devices.

![Studio_Gallery](media/wireframes/desktop_wireframe.png)
![Studio_Gallery](media/wireframes/product_desktop.png)
![Studio_Gallery](media/wireframes/tablet_wireframe.png)
![Studio_Gallery](media/wireframes/mobile_wireframe.png)

## Future Goals

There are various improvements I would like to undertake in future. Unfortunately due to time constraints a number of ideas I wished to undertake did not come to fruition. There is code in the artists folder for example ready for future development. This was originally intended to be part of the project but it was decided to have the site working rather than spending time on additional functionality.

Other future goals include:
      - Uploading more work by more artists.
      - The option to search by a particular colour or theme.
      - Creating a profile page for each artist. 

## Technology Used

* HTML
* CSS
* Javascript
* Python

# Deployment

Django was used throughout the project. It is necessary to install Django to create the apps reuired to run the site.

Set up Elephant SQL for project

Set up Heroku for project

Link Elephant SQL with Heroku project area. 

Set up AWS with necessary S3 bucket for static files, policy, group, user and link with appropriate keys to heroku.

Ensure all necessary keys - secret and public are stored in config vars on Heroku.

Add new webhook endpoint to Stripe for Heroku. 

# Credits

This work was based on the Boutique Ado project by Code Institute, without which this project would not have gotten as far as it did.

A huge thank you to my mentor Richard without whom I would have not managed to submit anything. 

Communities on Slack, Stack Overflow and various other websites - too many to recall without whom I would have failed to get anything working at various points.

Regretfully I ran out of time long before this project was finished and my work reflects that. All mistakes are very much my own.










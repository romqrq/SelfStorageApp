#Storage - Self storage app

## Introduction

[Storage](https://romqrq.github.io/SelfStorageApp/) is an application that has the proposal to be a platform where users can view, book and create self storage units.

## Table of Contents

1. [UX](#ux)

   - [User Stories](#user-stories)
     - [Customer Stories](#customer-stories)
     - [Operator Stories](#operator-stories)

2. [Features](#features)

   - [Existing Features](#existing-features)
     - [Elements common to every Page](#elements-common-to-every-page)
     - [Home Page](#home-page)
     - [Booking Page](#booking-page)
     - [Admin Page](#admin-page)

3. [Information Architecture](#information-architecture)

   - [Database choice](#database-choice)
   - [Data Storage Types](#data-storage-types)
   - [Collections Data Structure](#collections-data-structure)

     - [Units Collection](#units-collection)
     - [Bookings Collection](#bookings-collection)

4) [Technologies Used](#technologies-used)

   - [Tools](#tools)
   - [Libraries](#libraries)
   - [Languages](#languages)

5) [Testing](#testing)

6) [Deployment](#deployment)

   - [Heroku Deployment](#heroku-deployment)
   - [How to run this project locally](#how-to-run-this-project-locally)

7) [Credits](#credits)

   - [Images](#images)
   - [Code](#code)

---

# UX

## User Stories

### Customer Stories

1. I can navigate to "/" to see a list of available Units with their size in square feet and price/
2. I can start a Booking by selecting a Unit on "/". This will link to "/bookings/new".
3. I can submit a Booking (on /bookings/new) by entering my email, name and address plus a move in date. Clicking Save will save the booking and redirect back to the root url "/" with a flash message (banner) to confirm a successful save.
4. When I successfully place a booking I should be redirected back to "/" with a banner confirming the booking was successfully created.

### Operator Stories

As a service provider I want:

1. I can create a new Unit, from "/admin/units/new" which has a name, size and a price (these are the units that will be listed on the root url page "/").

# Features

## Existing Features

### Elements common to all pages

- Navigation bar
  - The navigation bar is fixed at the top of the screen, always visible and is responsive to screen size.
  - On the left side the menu offers all the navigation options for the user to go from one page to another.
  - On small resolution screens, the menu goes under a "hamburger" button.
  - At the center, the "Storage" logo is linked to the index page and it holds an attention grabbing place while leaving the more accessible to touch edges for the menu and buttons.

- Footer

  - On the left, is displayed a short text about the purpose and mission of the website.
  - On the right, a list of the social media links. Currently the links are pointing to the respective home page for that social media platforms.
  - Copyright information.

### Home Page

- On this page the user can find a list of the Units on the database with the respective "Book" button directing to the booking page.
- On the second part of the page the admin section is also accessible through the "Create Unit" button.

### Booking Page

- On this page the user can find:
    - A card with the information of the unit to be booked.
    - A "choose another unit" button that brings the user back to the home page.
    - A form containing the requested information to proceed with the booking.

### Admin Page

- On this page the user can find:
    - A form containing the requested information to create a new unit.
    - A list of cards with the information of the unit that already exist on the database.

# Information Architecture

## Database Choice

This project is based on a pre-existing NoSQL MongoDB database structure. This project was molded to suit better the database characteristics due to time constraints but it could also have been based on a SQL database structure.

### Data Storage Types

The types of data stored in MongoDB for this project are:

- ObjectId
- String

### Collections Data Structure

Storage database structure is based on two collections:

#### Units Collection

| Title           | Key in db        | Form Validation Type   | Data Type |
| --------------- | ---------------- | ---------------------- | --------- |
| Unit ID         | \_id             | None                   | ObjectId  |
| Unit Name       | unit_name        | text, `maxlength="40"` | string    |
| Unit Size       | unit_size        | text, `maxlength="40"` | string    |
| Unit Price      | unit_price       | float field            | float     |


#### Bookings Collection

| Title           | Key in db       | Form Validation Type  | Data Type |
| --------------- | --------------- | --------------------- | --------- |
| Booking ID      | \_id            | None                  | ObjectId  |
| User Name       | user_name       | text, `maxlength="40"`| string    |
| Adress          | address         | text, `maxlength="40"`| string    |
| Email           | email           | email field           | string    |
| Move in Date    | move_in_date    | text                  | string    |
| Unit            | unit            | None                  | ObjectId   |


- The Unit field is retrieved from the parameters sent through the URL after the user user selects the unit from index.


# Technologies Used

## Tools

- [Gitpod](https://www.gitpod.io/) is the main IDE used for developing this project.
- [Visual Studio Code](https://code.visualstudio.com/) was also used as IDE for development when Gitpod wasn't available.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/) to handle version control.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database for this project
- [GitHub](https://github.com/) to store and share all project code remotely.
- [GIMP](https://www.gimp.org/) to edit, crop and save images.
- [Compress or die](https://compress-or-die.com/) website used to compress image files.

## Libraries

- [Materialize](https://materializecss.com/) to provide icons and a consistent and responsive structure to the website.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [PyMongo](https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible.
- [Flask](https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages.
- [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in html.

## Languages

- [HTML](https://html.com/).
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS).
- [Python](https://www.python.org/).

# Testing

Testing information can be found in separate [TESTING.md](TESTING.md) file

# Deployment

## Heroku Deployment

To deploy this application to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `web: python src/app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region you prefer.

5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the heroku app to the correct GitHub repository.

7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8. Set the following config vars:

| Key        | Value                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| DEBUG      | FALSE                                                                                                              |
| IP         | 0.0.0.0                                                                                                            |
| MONGO_URI  | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority` |
| PORT       | 5000                                                                                                               |
| SECRET_KEY | `<your_secret_key>`                                                                                                |

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

9. In the heroku dashboard, click "Deploy".

10. In the "Manual Deployment" section of this page, make sure the master branch is selected and then click "Deploy Branch".

11. The site is now successfully deployed.

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:

- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:

- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine.
  - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

### Instructions

1. Save a copy of the github repository located at `https://github.com/romqrq/SelfStorageApp` by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

```
git clone https://github.com/romqrq/SelfStorageApp
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, for this project, I used Anaconda. Enter the command:

```
python -m .venv venv
```

_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:

```
.venv\Scripts\activate
```

_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with

```
pip install --upgrade pip.
```

6. Install all required modules with the command

```
pip -r requirements.txt.
```

7. In your local IDE create a file called `.flaskenv`.

8. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database the same name used when setting up your environment variables ("MONGODB_NAME"), with 2 collections called `stora_units` and `stora_bookings`.

9. You can now run the application with the command

```
python src/app.py
```

10. You can visit the website at `http://127.0.0.1:5000`

# Credits

### Images

- [Images source (non existing link)](https://nolink.nolink/)

## Code

- For [MongoDB - Atlas](https://www.mongodb.com/), [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Python](https://www.python.org/doc/) the documentation on official websites was constantly used to learn how to use functionalities and avoid deprecated terms and expressions.

- Page components such as buttons, navbar, footer, sidenav and others were taken from [Materialize CSS](https://materializecss.com) and modified to suit the applications needs.

- The code for the parallax feature was taken from [Materialize - Parallax](https://materializecss.com/parallax.html) and edited to fit images better on different screen sizes.

- Code for the pulse effect on buttons was taken from [Materialize - Pulse](https://materializecss.com/pulse.html) and edited to match the style of the application.

## Acknowledgements

I would like to thank my mentor [Simen Daehlin](https://github.com/Eventyret) for pushing me and setting higher standards to push me out of my comfort zone and excel. Simen has also been a great guide as to what is expect from me as a professional, what is expected of my code and my applications.
I would like to thank [Anna Greaves](https://github.com/AJGreaves) for allowing me to use her documentation as a reference to build mine. As a student it is hard to start something when you have no reference and Anna has been a great reference as a successful fellow student.

I also would like to thank my fiance Rebecca Martin for being so patient and supportive when I'm spending endless hours on the computer. All this work is result of our teamwork and her belief on me starting a new career.

# Contact

To contact me feel free to email

`rjaalbuquerque (at) gmail (dot) com`

## Disclaimer

The content of this website is educational purposes only.
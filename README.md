# visual-business-pro
Visual Business Pro is a website that allows business owners to track various day-to-day business
metrics and have them displayed as interactive data visualisations using d3, the intended purpose would be to allow business
managers to home in on key metrics and see what was performing best and when, or what losses occured, why and when. It also allows
employers to track employees.

Hosted location -> https://visualbusinesspro.herokuapp.com/
# please use the following login details to view pre-populated dashboards
# email: alanjmurphy91@gmail.com , password: alan

Of course for review purposes and to test registration code please feel free to make a new account using credit card no.  4242424242424242


# Django
I created a base django (v1.11) project in python v2.7.14 with a virtual environment to begin. Inside this are two apps. The first provides for the home page and navigation
and the second contains the sites functionality. I decomposed the original settings.py file into base, dev and staging files.
Firstly I overrided the user and auth model settings to create a custom user model which used email instead of username. I then created models and forms
for each of the dashboards on the site, each referencing the user id as a primary key and filtering the objects by user. This is an 
extremely important step as otherwise any user could access the data of another. Similarly when creating the deletion forms I created
an instance on the user_id before getting whatever primary key was necessary to submit the delete form. I have also included some unit tests to ensure
sound functionality.

I relied heavily on djangos rest API framework in this project and this can be seen in the model serialiser files and the API view classes in
profile views. This allowed me to access the backend as JSON and feed it to the crossfilter instance running in a clients browser.

# HTML/CSS

I created a base html template which included all of my css and js. Any additional html files were extensions of this. 
The site uses bootstraps grid and then css grid for fine adjustment. The most important being setting the wrapper divs
for the d3 div's as grids and aligning to centre the axis and row. This allows for a nice centred display in the div
on desktops and laptops. I used a lot of inline styling for this project as it was quite
convenient when each div wanted slightly different css attributes. 

# JavaScript

The first piece of js code in the project is the jquery file from stream 3 which tests a users credit card. This is an important detail as it stops
a user from inputting their details twice. The bulk of the javascript used in this project is the d3 stack which was covered in stream 2.
As in my last project, im using d3, dc and crossfilter to generate the data visualisations. Crossfilter uses the django rest api to get
its data and then I set up my dims. I had a confusing problem initially in that the automatic timestamp from the django model didnt work
with d3. As it happens the d3 date parser produces a value quite a bit different and as such ive included at the top of every dashboard
file a for each function that slices the d/m/y from the string that wasn't working and parses it into something d3 liked. Apart from
that everything worked as intended and the data is interactive.

# Responsive

The site displays as expected on mobile and tablet thanks to bootstraps grid system. The barcharts that signify dates tended
to overflow on the x-axis on responsive devices so I used malihu's nice scrollbar plugin to allow for overflow instead of the ugly default one. I
didn't have to use any media queries for this project as the grid and css grid covered everything.

# Hosting

The app is currently served on heroku and connected to this repository. In order to do this I created a runtime file, to declare 
python 2.7 environment and requirements.txt in root ensured the necessary libraries were imported. I then 'scaled my dynos' with the Procfile.
I initially had trouble with this as I had the procfile one level too high for heroku to see.

# References/Credit

I based the auth code and stripe card jquery off material from the course, I believe this is Aaron Sinnot or Alisa Kennedys code. There wasn't any point in reinventing the wheel here so just used what worked in the course.
The custom scrollbar is by Milahu http://manos.malihu.gr/jquery-custom-content-scroller/



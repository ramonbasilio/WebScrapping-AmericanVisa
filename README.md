# WebScrapping-AmericanVisa

Getting a visa is the dream of many people around the world, but during the Covid 19 pandemic, getting data available at the Consulate is almost always distant.

With that in mind, I developed this script in Python to automatically enter the American Visa scheduling website, check a closer date and send the information relevant to the search carried out by the script in your email.

This design can be improved and improved.

For this project 3 classes were created and each class has a specific role.

class AmericanVisaAccess
This class's role is to log into the site and check the nearest available date. As a parameter of the constructor it receives the user's email and password. The class has 3 methods: checkFileIsCreated( ), seeNextIndex( ) and proximityParameter( ).



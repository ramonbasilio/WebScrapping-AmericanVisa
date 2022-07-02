# WebScrapping-AmericanVisa
Getting a visa is the dream of many people around the world, but during the Covid 19 pandemic, getting data available at the Consulate is almost always distant.

With that in mind, I developed this script in Python to automatically enter the American Visa scheduling website, check a closer date and send the information relevant to the search carried out by the script in your email.

This design can be improved and improved.

## About the scripts
For this project 3 classes were created and each class has a specific role.

## class AmericanVisaAccess
This class's role is to log into the site and check the nearest available date. As a parameter of the constructor it receives the user's email and password. The class has 3 methods: checkFileIsCreated( ), seeNextIndex( ) and proximityParameter( ).

checkFileIsCreated( ) checks if the file "SheetData.xlsx" exists. If it has not been created, the method creates the file.

seeNextIndex( ) checks the next index to control the worksheet.

proximityParameter( ) returns a number (in days) that is the subtraction of the nearest available date and the first day of the year 2022.

## class save
This class saves the following data in the worksheet:

index > Search index (integer starting at 2)

currentMonth > Month of date available

currentYear > Year of available date

totalDays > Number of days available

availableDays > Available days

firstClosestDate > The closest available date

proximityParameter > Proximity parameter


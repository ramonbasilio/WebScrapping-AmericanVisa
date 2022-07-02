# WebScrapping-AmericanVisa
Getting a US Visa is the dream of many people around the world, but during the Covid 19 pandemic, getting data available at the Consulate is almost always distant.

With that in mind, I developed this script in Python to automatically enter the American Visa scheduling website, check a closer date and send the information relevant to the search carried out by the script in your email.

This design can be improved and improved.

## About the scripts
For this project 4 classes were created and each class has a specific role.

## 1. class AmericanVisaAccess
This class's role is to log into the site and check the nearest available date. As a parameter of the constructor it receives the user's email and password. The class has 3 methods: checkFileIsCreated( ), seeNextIndex( ) and proximityParameter( ).

* checkFileIsCreated( ) checks if the file "SheetData.xlsx" exists. If it has not been created, the method creates the file.

* seeNextIndex( ) checks the next index to control the worksheet.

* proximityParameter( ) returns a number (in days) that is the subtraction of the nearest available date and the first day of the year 2022.

## 2. class save
This class saves the following data in the worksheet:

* **index**: Search index (integer starting at 2)
* **currentMonth**: Month of date available
* **currentYear**: Year of available date
* **totalDays**: Number of days available
* **availableDays**: Available days
* **firstClosestDate**: The closest available date
* **proximityParameter**: Proximity parameter

## 3. class sendEmail
This class sends the email with the information previously saved in the worksheet.\
When instantiating this class, in addition to passing the data saved in the worksheet, the user must pass an email address (gmail) with the sender pass for sending and another email that will receive the content.

See below a example:
![image_email](https://user-images.githubusercontent.com/37743546/176981532-379a7260-986a-477c-9e92-018d40bf02ee.png)

## 4. class alert
This class returns if there is an earlier date.

## main
The main file is reserved to instantiate the classes and declare the email and password for accessing the US visa scheduling website and also the emails and sender pass of the sendEmail class constructor.

## dictionaryDaysMonths
Not least there is a file with a simple dictionary to convert the months into the respective days of the month.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------

_Developed by Ramon Basilio_\
_July/2022_

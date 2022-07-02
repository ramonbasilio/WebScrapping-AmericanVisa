from webScrapping import AmericanVisaAccess
from saveOnSheet import save
from sendEmailAlert import sendEmail
from nearestDateAlert import alert

email = "ramon.basilio@hotmail.com"
password = "gta5632bv"

sender_address = 'ramon.s.basilio@gmail.com'
sender_pass = 'cuxmtgrivlddkyiu'
receiver_address = 'ramon.basilio@hotmail.com'

myAutomationWeb = AmericanVisaAccess(email, password)
myAutomationWeb.checkFileIsCreated()

index = myAutomationWeb.seeNextIndex()
currentMonth = myAutomationWeb.currentMonth
currentYear = myAutomationWeb.currentYear
totalDays = myAutomationWeb.totalDays
availableDays = myAutomationWeb.availableDays
firstClosestDate = myAutomationWeb.firstClosestDate
proximityParameter = myAutomationWeb.proximityParameter()

alerting = alert(index, proximityParameter)
alertReturn = alerting.nearestDateAlert()

saving = save(index, currentMonth, currentYear, totalDays,
              availableDays, firstClosestDate, proximityParameter)
sending = sendEmail(firstClosestDate, totalDays,
                    availableDays, currentMonth, currentYear, alertReturn, sender_address, sender_pass, receiver_address)

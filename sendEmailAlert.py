from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import smtplib


class sendEmail():
    def __init__(self,
                 firstClosestDate,
                 totalDays,
                 availableDays,
                 currentMonth,
                 currentYear,
                 alertReturn,
                 sender_address,
                 sender_pass,
                 receiver_address):

        self.currentDate = str(datetime.now())[:16]
        self.firstClosestDate = firstClosestDate
        self.totalDays = totalDays
        self.availableDays = availableDays
        self.currentMonth = currentMonth
        self.currentYear = currentYear
        self.alertReturn = alertReturn
        self.sender_address = sender_address
        self.sender_pass = sender_pass
        self.receiver_address = receiver_address

        mail_content = f"""
        Search Day: { self.currentDate}
        First Closest Date Available: {self.firstClosestDate}
        Number of Days Available: {self.totalDays}
        Days Available: {self.availableDays}
        Month: {self.currentMonth}
        Year: {self.currentYear}
        Alert: {self.alertReturn}
        """
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        # The subject line
        message['Subject'] = f"Automatic Email - Search Date Available for US Visa"
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain', "utf-8"))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        # login with mail_id and password
        session.login(self.sender_address, self.sender_pass)
        text = message.as_string()
        session.sendmail(self.sender_address, self.receiver_address, text)
        session.quit()
        print('Mail Sent')

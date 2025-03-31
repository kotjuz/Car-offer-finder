import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os



class EmailManager():
    def __init__(self):
        load_dotenv()
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.password = os.getenv("SENDER_PASSWORD")
        self.receiver_email = os.getenv("RECEIVER_EMAIL")

    def get_email(self):
        return self.sender_email, self.password

    def send_mail(self, car_list):
        self.car_list = car_list
        self.message = MIMEMultipart("alternative")
        self.text=""""""
        self.html=""""""

        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

        self.message["Subject"] = "Nowe auta!"
        self.text = """\
        Blad wyslania wiadomosci"""
        self.html = f"""\
        <html>
          <body>
        """

        for car in self.car_list:
            self.html = self.html + (f"<p>{car['name']}<br>"
                           f"Cena: {car['details']['price']}<br>"
                           f"Rocznik: {car['details']['year']}<br>"
                           f"Przebieg: {car['details']['mileage']}<br>"
                           f"<a href={car['details']['ad_link']}>Link do ogloszenia</a>"
                           f"</p> \n")

        self.html=self.html+('</body>\n'
           '</html>\n')

        part1 = MIMEText(self.text, "plain")
        part2 = MIMEText(self.html, "html")

        self.message.attach(part1)
        self.message.attach(part2)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(
                    self.sender_email, self.receiver_email, self.message.as_string()
                )
        except Exception:
            print("Unable to send an email")
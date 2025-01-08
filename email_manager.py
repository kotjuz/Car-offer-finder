import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

class EmailManager():

    def __int__(self):
        pass


    def send_mail(self, car_list):
        self.sender_email = "pythoncourse.testmail1@gmail.com"
        self.password = "ysowerrknadupvwg"
        self.receiver_email = "rafalcriscars@gmail.com"
        self.car_list = car_list
        self.message = MIMEMultipart("alternative")
        self.text=""""""
        self.html=""""""
        # self.message["Subject"] = "multipart test"
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
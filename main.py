from scrap_manager import ScrapManager
from data_manager import DataManager
from email_manager import EmailManager
import time


scrap_manager = ScrapManager()
data_manager = DataManager(scrap_manager.data_list)
email_manager = EmailManager()

scrap_manager.get_whole_page_mobilede()


for i in range(60):
    interesting_cars = []
    scrap_manager.get_whole_page_schadeautos()
    interesting_cars.extend(data_manager.check_for_new_cars(scrap_manager.data_list))
    if len(interesting_cars)>0:
        print(interesting_cars)
        email_manager.send_mail(interesting_cars)
    time.sleep(240)

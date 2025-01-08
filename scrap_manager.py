from bs4 import BeautifulSoup
import requests


class ScrapManager():

    def __init__(self):
        self.data_list=[]
        self.get_whole_page()

    def get_whole_page(self):
        self.data_list = []
        response = requests.get("https://www.schadeautos.nl/pl/szukaj/uszkodzony/samochody-osobowe/1/1/0/0/0/0/1/0")
        response.raise_for_status()
        schadeautos = response.text
        schade_soup = BeautifulSoup(schadeautos, "html.parser")
        ad_div = schade_soup.find_all(name="div", class_="car-inner flexinner")
        car_names = [div.find(name="h2").find(name="a").get_text() for div in ad_div]

        car_year = schade_soup.find_all(name="div", title="data pierwszej rejestracji")
        car_years = [year.get_text() for year in car_year]

        car_mileage = schade_soup.find_all(name="div", title="przebieg")
        car_mileages = [mileage.get_text() for mileage in car_mileage]

        car_ad_link = schade_soup.find_all(name="div", class_="car-image text-center")
        car_ad_links = [links.find(name="a").get("href") for links in car_ad_link]

        car_price = schade_soup.find_all(name="div", class_="price")
        car_prices = [price.get_text() for price in car_price]
        if len(car_prices) < len(car_ad_links):
            for i in range(len(car_prices), len(car_ad_links)):
                car_prices.append("Nie podana")

        if len(car_years) < len(car_ad_links):
            for i in range(len(car_years), len(car_ad_links)):
                car_years.append("Nie podana")

        if len(car_mileage) < len(car_ad_links):
            for i in range(len(car_mileage), len(car_ad_links)):
                car_mileages.append("Nie podana")

        if len(car_names) < len(car_ad_links):
            for i in range(len(car_names), len(car_ad_links)):
                car_names.append("Nie podana")


        for i in range(0, len(car_ad_links)):
                self.data_list.append({
                    "name":car_names[i],
                    "details":{
                    "price": car_prices[i],
                    "year": car_years[i],
                    "mileage": car_mileages[i],
                    "ad_link": f"https://www.schadeautos.nl{car_ad_links[i]}",
                }
            })
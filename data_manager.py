class DataManager():
    def __init__(self, database):
        self.database=database
        self.interesting_brands=["peugeot","mercedes","volkswagen", "citroen", "toyota", "kia", "bmw", "audi", "seat", "opel", "skoda", "volvo", "renault", "dacia"]

    def check_for_new_cars(self, current_page_list):
        new_cars=[]

        current_database_ad_links = [car["details"]["ad_link"] for car in self.database]

        for car in current_page_list:
            if car["details"]["ad_link"] not in current_database_ad_links:
                new_cars.append(car)
                self.database.insert(0, car)
                self.database.pop(12)
        if len(new_cars) > 0:
            return self.check_for_interesting_cars(new_cars)
        else:
            return []

    def check_for_interesting_cars(self, new_cars):
        interesting_cars = []
        for car in new_cars:
            brand = car["name"].split()[0]
            if brand.lower() in self.interesting_brands:
                interesting_cars.append(car)
        return interesting_cars



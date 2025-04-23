class DataManager():
    def __init__(self, database):
        self.database=database
        self.interesting_properties = {
            "brands": ["peugeot","mercedes","volkswagen", "citroen", "toyota", "kia", "bmw", "audi", "seat", "opel", "skoda", "volvo", "renault", "dacia"],
            "min_price": 100,
            "max_price": 30000,
            "min_year": 2000,
            "max_year": 2026,
            "max_mileage": 300000
        }

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
            matches = 0
            brand = car["name"].split()[0]
            if brand.lower() in self.interesting_properties["brands"]:
                matches += 1
            if self.interesting_properties["min_price"] <= car['price'] <= self.interesting_properties["max_price"]:
                matches += 1
            if self.interesting_properties["min_year"] <= car['year'] <= self.interesting_properties["max_year"]:
                matches += 1
            if car['mileage'] <= self.interesting_properties["max_mileage"]:
                matches += 1

            if matches == 4:
                interesting_cars.append(car)
                
        return interesting_cars



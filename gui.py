import json
from tkinter import *
from tkinter import messagebox

class ApplicationGui():
    def __init__(self):
        self.window = Tk()
        self.entries = []
        self.interesting_properties = {}
        self.window.title("Filtry")
        self.window.config(bg="white", padx=20, pady=20, width=500, height=350)
        self.window.minsize(500, 350)
        self.window.maxsize(500, 350)

        self.read_properties_from_file()
        self.page_config()
        self.window.mainloop()

    def save_properties(self):
        print("HEJ")
        self.interesting_properties = {
            "brands": ["peugeot","mercedes","volkswagen", "citroen", "toyota", "kia", "bmw", "audi", "seat", "opel", "skoda", "volvo", "renault", "dacia"],
            "min_price": self.entries[0].get(),
            "max_price": self.entries[1].get(),
            "min_year": self.entries[2].get(),
            "max_year": self.entries[3].get(),
            "max_mileage": self.entries[4].get()
        }
        with open("properties_config.json", "w") as file:
            file.write(json.dumps(self.interesting_properties))

        messagebox.showinfo(message="Zapisano zmiany")
        self.window.destroy()

    def read_properties_from_file(self):
        with open("properties_config.json", "r") as file:
            self.interesting_properties = json.loads(file.read())

    def get_properties(self):
        return self.interesting_properties


    def page_config(self):

        min_price_label = Label(self.window, text="Minimalna cena: ", bg="white")
        min_price_label.grid(row=1, column=1, sticky='w', columnspan=2, padx=10)
        min_price_entry = Entry(self.window, width=30, text)
        min_price_entry.grid(row=2, column=1, pady=10, padx=10)

        max_price_label = Label(self.window, text="Maksymalna cena: ", bg="white")
        max_price_label.grid(row=1, column=2, sticky='w', columnspan=2, padx=10)
        max_price_entry = Entry(self.window, width=30)
        max_price_entry.grid(row=2, column=2, pady=10, padx=10)

        min_year_label = Label(self.window, text="Minimalny rocznik: ", bg="white")
        min_year_label.grid(row=3, column=1, sticky='w', columnspan=2, padx=10)
        min_year_entry = Entry(self.window, width=30)
        min_year_entry.grid(row=4, column=1, pady=10, padx=10)

        max_year_label = Label(self.window, text="Maksymalny rocznik: ", bg="white")
        max_year_label.grid(row=3, column=2, sticky='w', columnspan=2, padx=10)
        max_year_entry = Entry(self.window, width=30)
        max_year_entry.grid(row=4, column=2, pady=10, padx=10)

        max_mileage_label = Label(self.window, text="Maksymalny przebieg: ", bg="white")
        max_mileage_label.grid(row=5, column=1, columnspan=2, padx=10)
        max_mileage_entry = Entry(self.window, width=30)
        max_mileage_entry.grid(row=6, column=1, columnspan=2, pady=10, padx=10)

        self.entries.extend([min_price_entry, max_price_entry, min_year_entry, max_year_entry, max_mileage_entry])

        confirm_button = Button(self.window, text="Zatwierdź", width=20, height=1, command=self.save_properties)
        confirm_button.grid(row=8, column=1, columnspan=2, padx=10)




app = ApplicationGui()
print(app.get_data())
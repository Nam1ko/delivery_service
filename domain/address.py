class Address:

    def __init__(self, city, street, house):
        self.city = city
        self.street = street
        self.house = house

    def get_full_address(self):
        return f"г. {self.city}, ул. {self.street}, дом {self.house}"
class Courier:

    def __init__(self, name, phone, vehicle):
        self.name = name
        self.phone = phone
        self.vehicle = vehicle

    def get_info(self):
        return f"Курьер: {self.name}, Телефон: {self.phone}, Транспорт: {self.vehicle}"
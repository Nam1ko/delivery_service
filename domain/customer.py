class Customer:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_info(self):
        return f"Клиент: {self.name}, Телефон: {self.phone}"
class Package:

    def __init__(self, description, weight):
        self.description = description
        self.weight = weight

    def get_info(self):
        return f"Посылка: {self.description}, Вес: {self.weight} кг"
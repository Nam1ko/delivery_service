from domain.order import Order
from domain.courier import Courier
from domain.address import Address

class Delivery:

    def __init__(self, order, courier, address):
        self.order = order
        self.courier = courier
        self.address = address

        self.status = "Ожидает отправки"

    def update_status(self, new_status):
        self.status = new_status

    def get_info(self):
        return (
            f"{self.order.get_info()}\n"
            f"{self.courier.get_info()}\n"
            f"Адрес доставки: {self.address.get_full_address()}\n"
            f"Статус: {self.status}"
        )
import math
from domain.customer import Customer
from domain.courier import Courier
from domain.address import Address
from domain.package import Package
from domain.order import Order
from domain.delivery import Delivery

class DeliveryService:

    def __init__(self, repository):
        self.repository = repository

    def create_delivery(
        self, order_id,
        customer_name, customer_phone,
        courier_name, courier_phone, vehicle,
        city, street, house,
        package_description, package_weight
    ):

        if not isinstance(order_id, int) or order_id <= 0:
            raise ValueError("Номер заказа должен быть положительным целым числом")

        for delivery in self.repository.get_all():
            if delivery.order.order_id == order_id:
                raise ValueError("Заказ с таким номером уже существует")

        text_fields = {
            "Имя клиента": customer_name,
            "Телефон клиента": customer_phone,
            "Имя курьера": courier_name,
            "Телефон курьера": courier_phone,
            "Транспорт": vehicle,
            "Город": city,
            "Улица": street,
            "Дом": house,
            "Описание посылки": package_description
        }

        for field, value in text_fields.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Поле «{field}» не может быть пустым")

        if (
                isinstance(package_weight, bool)
                or not isinstance(package_weight, (int, float))
                or not math.isfinite(package_weight)
                or package_weight <= 0
        ):
            raise ValueError("Вес должен быть положительным конечным числом")

        customer = Customer(customer_name, customer_phone)

        courier = Courier(courier_name, courier_phone, vehicle)

        address = Address(city, street, house)

        package = Package(package_description, package_weight)

        order = Order(order_id, customer, package)
        delivery = Delivery(order, courier, address)

        self.add_delivery(delivery)

        return delivery

    def add_delivery(self, delivery):
        order_id = delivery.order.order_id

        for existing in self.repository.get_all():
            if existing.order.order_id == order_id:
                raise ValueError("Заказ с таким номером уже существует")

        self.repository.add(delivery)

        try:
            self.repository.save()
        except OSError:
            self.repository.get_all().remove(delivery)
            raise

    def get_all_deliveries(self):
        return self.repository.get_all()

    def update_delivery_status(self, order_id, new_status):
        if not isinstance(new_status, str) or not new_status.strip():
            raise ValueError("Статус не может быть пустым")

        for delivery in self.repository.get_all():
            if delivery.order.order_id == order_id:
                old_status = delivery.status
                delivery.update_status(new_status.strip())

                try:
                    self.repository.save()
                except OSError:
                    delivery.update_status(old_status)
                    raise
                return True
        return False

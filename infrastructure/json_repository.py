import json

from domain.repository import Repository
from domain.customer import Customer
from domain.package import Package
from domain.order import Order
from domain.courier import Courier
from domain.address import Address
from domain.delivery import Delivery
from pathlib import Path

class JsonRepository(Repository):

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.deliveries = []
        self._load()

    def _load(self):
        if not self.file_path.exists():
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError(
                f"Файл {self.file_path} содержит некорректный JSON"
            ) from error

        if not isinstance(data, list):
            raise ValueError("В JSON-файле ожидался список доставок")

        try:
            for item in data:
                customer = Customer(
                    item["customer"]["name"],
                    item["customer"]["phone"]
                )

                courier = Courier(
                    item["courier"]["name"],
                    item["courier"]["phone"],
                    item["courier"]["vehicle"]
                )

                address = Address(
                    item["address"]["city"],
                    item["address"]["street"],
                    item["address"]["house"]
                )

                package = Package(
                    item["package"]["description"],
                    item["package"]["weight"]
                )

                order = Order(
                    item["order_id"],
                    customer,
                    package
                )

                delivery = Delivery(order, courier, address)

                delivery.status = item["status"]

                self.deliveries.append(delivery)
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(
                "В JSON-файле обнаружены некорректные данные доставки"
            ) from error

    def get_all(self):
        return self.deliveries

    def add(self, delivery):
        self.deliveries.append(delivery)

    def save(self):
        data = []

        for delivery in self.deliveries:
            data.append({
                "order_id": delivery.order.order_id,

                "customer":{
                    "name": delivery.order.customer.name,
                    "phone": delivery.order.customer.phone
                },

                "courier":{
                    "name": delivery.courier.name,
                    "phone": delivery.courier.phone,
                    "vehicle": delivery.courier.vehicle
                },

                "address": {
                    "city": delivery.address.city,
                    "street": delivery.address.street,
                    "house": delivery.address.house
                },

                "package":{
                    "description": delivery.order.package.description,
                    "weight": delivery.order.package.weight
                },

                "status": delivery.status
            })

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

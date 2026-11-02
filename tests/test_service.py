from infrastructure.json_repository import JsonRepository
from application.delivery_service import DeliveryService
from domain.customer import Customer
from domain.courier import Courier
from domain.address import Address
from domain.package import Package
from domain.order import Order
from domain.delivery import Delivery

repository = JsonRepository("test_service.json")
service = DeliveryService(repository)

customer = Customer("А", "+79871234567")
courier = Courier("B", "+77897654321", "Вело")
address = Address("Москва", "АБ", "1")
package = Package("Ноутбук", 2.5)

order = Order(1, customer, package)
delivery = Delivery(order, courier, address)

service.add_delivery(delivery)
print("Количество доставок:", len(service.get_all_deliveries()))

result = service.update_delivery_status(1, "В пути")
print("Статус обновлён:", result)
print("Новый статус:", service.get_all_deliveries()[0].status)
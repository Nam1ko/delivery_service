from infrastructure.json_repository import JsonRepository
from domain.customer import Customer
from domain.courier import Courier
from domain.address import Address
from domain.package import Package
from domain.order import Order
from domain.delivery import Delivery

customer = Customer("А", "+79871234567")
courier = Courier("B", "+77897654321", "Вело")
address = Address("Москва", "АБ", "1")
package = Package("Ноутбук", 2.5)

repository = JsonRepository("test_deliveries.json")

order = Order(1, customer, package)
delivery = Delivery(order, courier, address)

repository.add(delivery)

repository.save()

new_repository = JsonRepository("test_deliveries.json")

loaded_deliveries = new_repository.get_all()

print("Загружено доставок:", len(loaded_deliveries))

print(loaded_deliveries[0].order.customer.name)
print(loaded_deliveries[0].courier.name)
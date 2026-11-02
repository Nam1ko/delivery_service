from domain.delivery import Delivery


class Console:
    def __init__(self, delivery_service):
        self.delivery_service = delivery_service

    def show_menu(self):
        print("\n=== СЕРВИС ДОСТАВКИ ===")
        print("1. Показать все доставки")
        print("2. Изменить статус доставки")
        print("3. Сделать заказ")
        print("0. Выход")

    def show_deliveries(self):
        try:
            deliveries = self.delivery_service.get_all_deliveries()

            if not deliveries:
                print("Доставок пока нет")
                return

            for delivery in deliveries:
                print("--------------------")
                print(delivery.get_info())

        except OSError as error:
            print(f"Не удалось получить доставки: {error}")

    def update_status(self):
        order_id = int(input("Введите номер заказа: "))
        new_status = int(input("Введите новый статус: "))

        try:
            result = self.delivery_service.update_delivery_status(
                order_id, new_status
            )

            if result:
                print("Статус успешно изменён!")
            else:
                print("Ошибка: доставка не найдена.")

        except (ValueError, OSError) as error:
            print(f"Не удалось изменить статус: {error}")

    def create_delivery(self):
        print("\n=== СОЗДАНИЕ ЗАКАЗА ===")

        order_id = int(input("Номер заказа: "))

        print("\n--- Данные клиента ---")
        customer_name = input("Имя клиента: ")
        customer_phone = input("Телефон клиента: ")

        print("\n--- Данные курьера ---")
        courier_name = input("Имя курьера: ")
        courier_phone = input("Телефон курьера: ")
        vehicle = input("Транспорт курьера: ")

        print("\n--- Адрес доставки ---")
        city = input("Город: ")
        street = input("Улица: ")
        house = input("Дом: ")

        print("\n--- Данные посылки ---")
        package_description = input("Описание посылки: ")
        package_weight = float(input("Вес посылки (кг): "))

        try:
            self.delivery_service.create_delivery(
                order_id,
                customer_name, customer_phone,
                courier_name, courier_phone, vehicle,
                city, street, house,
                package_description, package_weight
            )

            print("\nЗаказ успешно создан!")

        except (ValueError, OSError) as error:
            print(f"\nНе удалось создать заказ: {error}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите действие: ")

            try:
                if choice == "1":
                    self.show_deliveries()
                elif choice == "2":
                    self.update_status()
                elif choice == "3":
                    self.show_deliveries()
                elif choice == "0":
                    print("Программа завершена")
                    break
                else:
                    print("Пункт не найден")
            except (ValueError, OSError) as error:
                print(f"Ошибка: {error}")
from infrastructure.json_repository import JsonRepository
from application.delivery_service import DeliveryService
from presentation.console import Console

def main():
    try:
        repository = JsonRepository("deliveries.json")

        delivery_service = DeliveryService(repository)

        console = Console(delivery_service)

        console.run()

    except (ValueError, OSError) as error:
        print(f"Ошибка запуска программы: {error}")

if __name__ == "__main__":
    main()
class Order:

    def __init__(self, order_id, customer, package):
        self.order_id = order_id
        self.customer = customer
        self.package = package

    def get_info(self):
        return(
            f"Заказ №{self.order_id}\n"
            f"{self.customer.get_info()}\n"
            f"{self.package.get_info()}"
        )
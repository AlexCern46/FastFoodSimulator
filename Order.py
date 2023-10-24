orders = list()


class Order:
    def __init__(self, order_number):
        self.order_number = order_number

    def __str__(self):
        return f"Заказ № {self.order_number}"

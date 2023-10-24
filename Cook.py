import time
import Order
import Server


class Cooker:
    def __init__(self, name, cook_time):
        self.name = name
        self.cook_time = cook_time
        self.order = None

    def cooking(self):
        while True:
            if len(Order.orders) > 0:
                self.order = Order.orders.pop(0)
                time.sleep(self.cook_time)
                Server.ready_orders.append(self.order)
                self.order = None
            else:
                time.sleep(1)

    def get_info(self):
        return f"{self.name} {self.order}"

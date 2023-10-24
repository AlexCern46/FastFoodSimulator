import random
import time
import Order
import Server


customers = list()


class OrderTaker:
    def __init__(self, name, make_order_time):
        self.name = name
        self.customer = None
        self.make_order_time = make_order_time

    def make_order(self):
        while True:
            if len(customers) > 0:
                self.customer = customers.pop(0)
                time.sleep(self.make_order_time)
                order = Order.Order(random.randint(1, 100))
                self.customer.set_order_number(order)
                Order.orders.append(order)
                Server.waiting_customer.append(self.customer)
                self.customer = None
            else:
                time.sleep(1)

    def get_info(self):
        return f"{self.name} {self.customer}"

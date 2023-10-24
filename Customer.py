import random
import time
import OrderTaker


flag = False


def get_name():
    names = ["Павел", "Анна", "Михаил", "Ольга", "Андрей", "Наталья", "Александр", "Екатерина", "Иван", "Мария"]
    return random.choice(names)


def make_customer(interval):
    global flag

    while flag:
        time.sleep(interval)
        customer = Customer(get_name())
        OrderTaker.customers.append(customer)


class Customer:
    def __init__(self, name):
        self.name = name
        self.order_number = None

    def set_order_number(self, order_number):
        self.order_number = order_number

    def __str__(self):
        return f"{self.name} {self.order_number}"

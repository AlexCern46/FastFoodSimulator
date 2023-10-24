import time


waiting_customer = list()
ready_orders = list()


class Server:
    def __init__(self, name, serer_time):
        self.name = name
        self.order = None
        self.serer_time = serer_time

    def extradition_order(self):
        while True:
            if len(ready_orders) > 0:
                for order in ready_orders:
                    ready_orders.remove(order)
                    for customer in waiting_customer:
                        if order == customer.order_number:
                            self.order = order
                            time.sleep(self.serer_time)
                            waiting_customer.remove(customer)
                            self.order = None
                            break
            else:
                time.sleep(1)

    def get_info(self):
        return f"{self.name} {self.order}"

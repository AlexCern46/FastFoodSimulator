import tkinter as tk
import Customer
import OrderTaker
import Order
import Cook
import Server
import threading


threads = list()
order_takers = list()
order_takers_thr = list()
cookers = list()
cookers_thr = list()
servers = list()
servers_thr = list()


def update_view():
    while True:
        count_to_order_taker_label.config(text=f"В очереди на приём заказов: {len(OrderTaker.customers)}")
        count_to_cook_label.config(text=f"В очереди на готовку: {len(Order.orders)}")
        count_to_take_label.config(text=f"В очереди на выдачу: {len(Server.ready_orders)}")
        cookers_listbox.delete(0, tk.END)
        for cooker in cookers:
            cookers_listbox.insert(tk.END, cooker.get_info())
        order_takers_listbox.delete(0, tk.END)
        for order_taker in order_takers:
            order_takers_listbox.insert(tk.END, order_taker.get_info())
        take_listbox.delete(0, tk.END)
        for server in servers:
            take_listbox.insert(tk.END, server.get_info())
        wait_listbox.delete(0, tk.END)
        for customer in Server.waiting_customer:
            wait_listbox.insert(tk.END, customer)


def start_button_click():
    Customer.flag = True

    try:
        cooking_time = float(cooking_time_entry.get())
        interval = float(interval_of_new_customers_entry.get())
        make_order_time = float(make_order_time_entry.get())
        server_time = float(server_time_entry.get())
        num_of_order_takers = int(num_of_order_takers_entry.get())
        num_of_cookers = int(num_of_cookers_entry.get())
        num_of_servers = int(num_of_servers_entry.get())

        if cooking_time <= 0 or interval <= 0 or make_order_time <= 0 or server_time <= 0 or num_of_order_takers <= 0 or num_of_cookers <= 0 or num_of_servers <= 0:
            raise Exception('Значение должно быть больше 0')

        for i in range(num_of_cookers):
            cooker = Cook.Cooker(f'Повар {i+1}', cooking_time)
            cookers.append(cooker)

        for i in range(num_of_order_takers):
            order_taker = OrderTaker.OrderTaker(f'Кассир {i + 1}', make_order_time)
            order_takers.append(order_taker)

        for i in range(num_of_servers):
            server = Server.Server(f'Официант {i + 1}', server_time)
            servers.append(server)

        for order_taker in order_takers:
            thread = threading.Thread(target=order_taker.make_order)
            order_takers_thr.append(thread)

        for cooker in cookers:
            thread = threading.Thread(target=cooker.cooking)
            cookers_thr.append(thread)

        for server in servers:
            thread = threading.Thread(target=server.extradition_order)
            servers_thr.append(thread)

        thread0 = threading.Thread(target=update_view)
        thread1 = threading.Thread(target=Customer.make_customer, args=(interval,))

        threads.append(thread0)
        threads.append(thread1)

        for thr in order_takers_thr:
            thr.start()

        for thr in cookers_thr:
            thr.start()

        for thread in threads:
            thread.start()

        for thr in servers_thr:
            thr.start()
    except Exception as e:
        error_window(f'Error: {e}')


def stop_button_click():
    Customer.flag = False


def error_window(text):
    error_window = tk.Toplevel(window)
    error_window.title('Error')
    error_label = tk.Label(error_window, text=text, font=('Arial', 14))
    error_label.pack()


window = tk.Tk()
window.title('Fast Food Simulator')
window.geometry('625x325')
window.resizable(False, False)

enter_label1 = tk.Label(window, text='Введите интервал появления новых клиентов (c):')
enter_label1.place(x=10, y=10)

interval_of_new_customers_entry = tk.Entry(window)
interval_of_new_customers_entry.place(x=10, y=30)

enter_label2 = tk.Label(window, text='Введите время приёма заказа (c):')
enter_label2.place(x=10, y=45)

make_order_time_entry = tk.Entry(window)
make_order_time_entry.place(x=10, y=65)

enter_label3 = tk.Label(window, text='Введите время приготовления (c):')
enter_label3.place(x=10, y=80)

cooking_time_entry = tk.Entry(window)
cooking_time_entry.place(x=10, y=100)

enter_label4 = tk.Label(window, text='Введите время выдачи заказов (c):')
enter_label4.place(x=10, y=115)

server_time_entry = tk.Entry(window)
server_time_entry.place(x=10, y=135)

enter_label5 = tk.Label(window, text='Введите число принимающих заказы:')
enter_label5.place(x=10, y=150)

num_of_order_takers_entry = tk.Entry(window)
num_of_order_takers_entry.place(x=10, y=170)

enter_label6 = tk.Label(window, text='Введите число поваров:')
enter_label6.place(x=10, y=185)

num_of_cookers_entry = tk.Entry(window)
num_of_cookers_entry.place(x=10, y=205)

enter_label7 = tk.Label(window, text='Введите число официантов:')
enter_label7.place(x=10, y=220)

num_of_servers_entry = tk.Entry(window)
num_of_servers_entry.place(x=10, y=240)

start_button = tk.Button(window, text='Старт', command=start_button_click)
start_button.place(x=10, y=270)

stop_button = tk.Button(window, text='Стоп', command=stop_button_click)
stop_button.place(x=100, y=270)

count_to_order_taker_label = tk.Label(window, text=f'В очереди на приём заказов: {0}')
count_to_order_taker_label.place(x=10, y=300)

count_to_cook_label = tk.Label(window, text=f'В очереди на готовку: {0}')
count_to_cook_label.place(x=300, y=10)

cookers_listbox = tk.Listbox(window)
cookers_listbox.place(x=300, y=30, width=150, height=140)

order_takers_listbox = tk.Listbox(window)
order_takers_listbox.place(x=300, y=175, width=150, height=140)

count_to_take_label = tk.Label(window, text=f'В очереди на выдачу: {0}')
count_to_take_label.place(x=465, y=10)

take_listbox = tk.Listbox(window)
take_listbox.place(x=465, y=30, width=150, height=140)

wait_listbox = tk.Listbox(window)
wait_listbox.place(x=465, y=175, width=150, height=140)

window.mainloop()

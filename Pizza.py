import  random
import customtkinter as ctk
from tkinter import Toplevel
from CTkMessagebox import CTkMessagebox
import time
from PIL import Image
import foto

class OnlineStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Онлайн Магазин")
        self.root.geometry("900x600")

        self.root.resizable(False, False)

        self.menu_frame = ctk.CTkFrame(self.root)
        self.menu_frame.pack(side=ctk.TOP, fill=ctk.X)

        self.search_entry = ctk.CTkEntry(self.menu_frame, placeholder_text="Пошук...")
        self.search_entry.pack(side=ctk.LEFT, padx=10)

        self.search_button = ctk.CTkButton(self.menu_frame, text="Пошук", command=self.search_product)
        self.search_button.pack(side=ctk.LEFT, padx=10)
        self.last_searched_product = None
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        self.create_menu()
        self.create_main_interface()

        self.switch_var = ctk.StringVar(value="off")
        self.switch = ctk.CTkSwitch(self.root, command=self.switch_event,
                                    variable=self.switch_var, onvalue="on", offvalue="off", text="Тема")
        self.switch.pack(anchor='ne')

        self.time_label = ctk.CTkLabel(root, text="", font=('Helvetica', 12))
        self.time_label.pack(side=ctk.BOTTOM, anchor='se', pady=10, padx=10)
        self.update_clock()

        self.show_menu()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S\n%D')
        self.time_label.configure(text=current_time)
        self.root.after(1000, self.update_clock)

    def create_menu(self):

        ctk.CTkButton(self.menu_frame, text="Меню", command=self.show_menu).pack(side=ctk.LEFT)
        ctk.CTkButton(self.menu_frame, text="Замовлення", command=self.show_orders).pack(side=ctk.LEFT)
        ctk.CTkButton(self.menu_frame, text="Новинки", command=self.show_new_products).pack(side=ctk.LEFT)
        ctk.CTkButton(self.menu_frame, text="Кошик", command=self.show_cart).pack(side=ctk.LEFT)

    def switch_event(self):
        if self.switch_var.get() == 'off':
            ctk.set_appearance_mode("dark")

        else:
            ctk.set_appearance_mode("light")

    def create_main_interface(self):
        self.products = [
            {"name": "Піца Грибна", "discount": "20%", "price": 230,
             "description": "Піца з грибами, сиром, томатним соусом та зеленню."},
            {"name": "Салат Морквяний", "discount": "30%", "price": 120,
             "description": "Салат з моркви, ізюму, горіхів та майонезу."},
            {"name": "Кола 0.5л", "discount": "15%", "price": 35, "description": "Освіжаючий напій зі смаком коли."},
            {"name": "Морозиво Кулькове", "discount": "65%", "price": 2,
             "description": "Морозиво в кульках з різними смаками: ваніль, шоколад, полуниця."},
            {"name": "Суші Макі", "discount": "25%", "price": 150,
             "description": "Суші з рисом, норі та свіжою рибою."},
            {"name": "Бургер Класичний", "discount": "10%", "price": 180,
             "description": "Класичний бургер з яловичиною, сиром, салатом та соусом."},
            {"name": "Смузі Фруктовий", "discount": "5%", "price": 90,
             "description": "Смузі з свіжих фруктів: банан, полуниця, манго."},
            {"name": "Кава Американо", "discount": "10%", "price": 50,
             "description": "Чорна кава без додатків."},
            {"name": "Піца з Куркою і Ананасом", "discount": "15%", "price": 250,
             "description": "Піца з куркою, ананасом, мацарелою та томатним соусом."},
            {"name": "Сендвіч з Ковбасою та Сиром", "discount": "10%", "price": 120,
             "description": "Сендвіч з ковбасою, сиром, майонезом та огірками."},
            {"name": "Гарячий Дог з Кетчупом і Гірчицею", "discount": "8%", "price": 70,
             "description": "Гарячий дог з ковбасою, кетчупом, гірчицею та цибулею."}
        ]
        self.product_menu = [

        ]
        self.ingridient = [
            {"name": "Помідор", "price": 7},
            {"name": "Курка", "price": 22},
            {"name": "Ананас", "price": 35},
            {"name": "Сир", "price": 9},
            {"name": "Мацарела", "price": 10, },
            {"name": "Сирний бортик", "price": 30, },
            {"name": "Меге піца 45см", "price": 90},
            {"name": "Ковбаска", "price": 9},
            {"name": "Соус", "price": 10},
            {"name": "зелень", "price": 2},
            {"name": "Цибулька", "price": 7}
        ]

        self.new_products = [
            {"name": "Суші Макі", "discount": "25%", "price": 150,
             "description": "Суші з рисом, норі та свіжою рибою."},
            {"name": "Бургер Класичний", "discount": "10%", "price": 180,
             "description": "Класичний бургер з яловичиною, сиром, салатом та соусом."},
            {"name": "Смузі Фруктовий", "discount": "5%", "price": 90,
             "description": "Смузі з свіжих фруктів: банан, полуниця, манго."},
            {"name": "Кава Американо", "discount": "10%", "price": 50,
             "description": "Чорна кава без додатків."}
        ]

        self.recently_added_products = [
            {"name": "Страва 1", "discount": "15%", "price": 200,
             "description": "Опис страви 1."},
            {"name": "Страва 2", "discount": "10%", "price": 150,
             "description": "Опис страви 2."},
            {"name": "Страва 3", "discount": "20%", "price": 180,
             "description": "Опис страви 3."}
        ]

        self.cart = []

    def show_menu(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.main_frame, text="Осінні Знижки", font=("Arial", 14)).pack(pady=10)
        for product in self.products:
            self.add_product_to_frame(product)

    def show_orders(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.main_frame, text="Замовлення", font=("Arial", 14)).pack(pady=10)

        # Створити кнопку "Створити свою піцу"
        ctk.CTkButton(self.main_frame, text="Створити свою піцу", command=self.create_custom_pizza).pack(pady=10)

        # Створити кнопку "Створити свій сет"
        ctk.CTkButton(self.main_frame, text="Створити свій сет", command=self.create_custom_set).pack(pady=10)

        # Додати три сірі квадрати в одну лінійку
        row_frame = ctk.CTkFrame(self.main_frame)
        row_frame.pack(side=ctk.TOP, pady=20)

        square_names = ["""Попробуй сам
                Ствои совє унікальне
                     смакуй по свому""", """Вибери дію 
                            Та користуйся своєю
                            уявою""", """А тепер час 
                            смакувати 
                                     Смачного """]

        for i, name in enumerate(square_names):
            square_frame = ctk.CTkFrame(row_frame, width=200, height=200, bg_color="grey", fg_color="grey")
            square_frame.pack(side=ctk.LEFT, padx=10)
            label = ctk.CTkLabel(square_frame, text=name, font=("Arial", 14), bg_color="grey", fg_color="grey")
            label.pack(expand=True, fill=ctk.BOTH)

    def create_custom_set(self):
        def add_to_cart(set_name, set_products, set_price):
            self.cart.append({"name": set_name, "products": set_products, "price": set_price})
            CTkMessagebox(title="Замовлення", message="Ваш сет додано до кошика", icon="check")
            custom_set_window.destroy()

        def order_custom_set():
            set_name = self.set_name_entry.get()
            if not set_name:
                CTkMessagebox(title="Помилка", message="Будь ласка, введіть назву сету!", icon="cancel")

                return

            set_products = [product['name'] for var, product in zip(checkbox_vars, self.products) if var.get()]
            set_price = sum(product['price'] for var, product in zip(checkbox_vars, self.products) if var.get())

            if not set_products:
                CTkMessagebox(title="Помилка", message="Будь ласка, виберіть хоча б один продукт!", icon="cancel")
                return
            # messagebox
            confirm = CTkMessagebox(title="Підтвердження замовлення",
                                    message=f"Загальна ціна: {set_price} грн\nЗамовити цей сет?",
                                    icon="question", option_2="No", option_3="Yes")

            if confirm:
                add_to_cart(set_name, set_products, set_price)

        custom_set_window = Toplevel(self.root)
        custom_set_window.title("Створити свій сет")
        custom_set_window.geometry("400x600")
        custom_set_window.configure(bg="green")

        label = ctk.CTkLabel(custom_set_window, text="Конструктор сету", font=("Arial", 18), bg_color="green")
        label.pack(pady=10)

        # Поле введення для назви сету
        self.set_name_entry = ctk.CTkEntry(custom_set_window, placeholder_text="Назва сету")
        self.set_name_entry.pack(pady=10)

        self.custom_set_products = []
        checkbox_vars = []

        # Додавання опцій для вибору продуктів
        for product in self.products:
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(custom_set_window,
                                       text=f"{product['name']} - {product['price'] + 40} грн, 40 грн корж",
                                       variable=var)
            checkbox.pack(anchor='w')
            checkbox_vars.append(var)

        # Кнопка "Замовити"
        order_button = ctk.CTkButton(custom_set_window, text="Замовити", command=order_custom_set)
        order_button.pack(pady=20)

    def create_custom_pizza(self):
        def add_to_cart(set_name, set_products, set_price):
            self.cart.append({"name": set_name, "products": set_products, "price": set_price})
            CTkMessagebox(title="Замовлення",
                          message=f"Ваша піца '{set_name}' з інгредієнтами: {', '.join(set_products)} додано до кошика!")

            custom_set_window.destroy()

        def order_custom_set():
            set_name = self.set_name_entry.get()
            if not set_name:
                CTkMessagebox(title="Помилка", message="Будь ласка, введіть назву піци!", icon="cancel")
                return

            set_products = [product['name'] for var, product in zip(checkbox_vars, self.ingridient) if var.get()]
            set_price = sum(product['price'] for var, product in zip(checkbox_vars, self.ingridient) if var.get())

            if not set_products:
                CTkMessagebox(title="Помилка", message="Будь ласка, виберіть хоча б один інгредієнт!", icon="cancel")
                return

            confirm = CTkMessagebox(title="Підтвердження замовлення",
                                    message=f"Загальна ціна: {set_price + 40} грн\nЗамовити цю піцу?",
                                    icon="question", option_2="No", option_3="Yes")
            if confirm:
                add_to_cart(set_name, set_products, set_price)

        custom_set_window = Toplevel(self.root)
        custom_set_window.title("Створити свою піцу")
        custom_set_window.geometry("400x600")
        custom_set_window.configure(bg="green")

        label = ctk.CTkLabel(custom_set_window, text="Конструктор піци", font=("Arial", 18), bg_color="green")
        label.pack(pady=10)

        self.set_name_entry = ctk.CTkEntry(custom_set_window, placeholder_text="Назва піци")
        self.set_name_entry.pack(pady=10)

        self.custom_set_products = []
        checkbox_vars = []

        for product in self.ingridient:
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(custom_set_window, text=f"{product['name']} - {product['price']} грн",
                                       variable=var)
            checkbox.pack(anchor='w')
            checkbox_vars.append(var)

        order_button = ctk.CTkButton(custom_set_window, text="Замовити", command=order_custom_set)
        order_button.pack(pady=20)

    def show_new_products(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.main_frame, text="Новинки", font=("Arial", 14)).pack(pady=10)

        image_paths = [
            "foto/pizza1.jpg",
            "foto/pizza2.jpg",
            "foto/pizza3.jpg",
            "foto/pizza4.jpeg"
        ]
        image_paths_dark = [
            "foto/pizza1_dark.jpg",
            "foto/pizza2_dark.jpg",
            "foto/pizza3.jpg",
            "foto/pizza4.jpeg"
        ]

        frame_top = ctk.CTkFrame(self.main_frame)
        frame_top.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, pady=5)
        frame_bottom = ctk.CTkFrame(self.main_frame)
        frame_bottom.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, pady=5)

        frames = [frame_top, frame_bottom]

        for i in range(len(image_paths)):
            img_path = image_paths[i]
            img_path_dark = image_paths_dark[i]

            img = Image.open(img_path)
            img_dark = Image.open(img_path_dark)

            img = img.resize((200, 200), Image.LANCZOS)
            img_dark = img_dark.resize((200, 200), Image.LANCZOS)

            img_ctk = ctk.CTkImage(light_image=img, dark_image=img_dark, size=(200, 200))

            label = ctk.CTkLabel(frames[i // 2], image=img_ctk, text="")
            label.image = img_ctk
            label.image_path = img_path
            label.pack(side=ctk.LEFT, padx=3, pady=3, expand=True, fill=ctk.BOTH)
            label.bind("<Button-1>", lambda event, path=img_path: print(f"Clicked on: {path}"))

    def show_cart(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.main_frame, text="Ваш Кошик", font=("Arial", 14)).pack(pady=10)

        total_price = 0
        for index, item in enumerate(self.cart):
            if 'products' in item:
                product_info = f"Піца: {item['name']}\nІнгредієнти: {', '.join(item['products'])}\nЦіна: {item['price']} грн"
            else:
                product_info = f"{item['name']} - ціна {item['price']} грн"

            frame = ctk.CTkFrame(self.main_frame)
            frame.pack(fill=ctk.X, pady=5)

            label = ctk.CTkLabel(frame, text=product_info, font=("Arial", 12), justify=ctk.LEFT)
            label.pack(side=ctk.LEFT, padx=10)

            delete_button = ctk.CTkButton(frame, text="❌", fg_color="red", width=10,
                                          command=lambda idx=index: self.remove_from_cart(idx))
            delete_button.pack(side=ctk.RIGHT, padx=5)

            total_price += item['price']

        total_label = ctk.CTkLabel(self.main_frame, text=f"Загальна вартість: {total_price} грн", font=("Arial", 14))
        total_label.pack(pady=10)

    def remove_from_cart(self, index):
        del self.cart[index]
        self.show_cart()

    def add_product_to_frame(self, product):
        frame = ctk.CTkFrame(self.main_frame)
        frame.pack(fill=ctk.X, pady=5)

        product_info = f"{product['name']} {product['discount']} знижки\nціна {product['price']} грн"
        label = ctk.CTkLabel(frame, text=product_info, font=("Arial", 12), justify=ctk.LEFT)
        label.pack(side=ctk.LEFT, padx=10)

        add_button = ctk.CTkButton(frame, text="Додати до кошика", command=lambda p=product: self.add_to_cart(p))
        add_button.pack(side=ctk.RIGHT, padx=10)

        detail_button = ctk.CTkButton(frame, text="Детальніше", command=lambda p=product: self.show_product_details(p))
        detail_button.pack(side=ctk.RIGHT, padx=10)

    def add_to_cart(self, product):
        self.cart.append(product)

        CTkMessagebox(title="Кошик", message=f"{product['name']} додано до кошика", icon="check")

    def show_product_details(self, product):
        CTkMessagebox(title="Детальніше", message=product["description"])

    def search_product(self):
        search_term = self.search_entry.get()
        if not search_term:  # Перевіряємо, чи поле введення порожнє
            CTkMessagebox(title="Пошук", message="Пошук пустий.", icon="cancel")

            return
        for product in self.products:
            if search_term.lower() in product['name'].lower():
                self.display_search_result(product)
                return
            CTkMessagebox(title="Пошук", message="Продукт не знайдено.", icon="cancel")

    def display_search_result(self, product):
        if hasattr(self, 'search_result_frame'):
            self.search_result_frame.destroy()

        self.search_result_frame = ctk.CTkFrame(self.root)
        self.search_result_frame.pack(side=ctk.TOP, fill=ctk.X, padx=10, pady=5)

        product_info = f"{product['name']} {product['discount']} знижки\nціна {product['price']} грн\n{product['description']}"
        label = ctk.CTkLabel(self.search_result_frame, text=product_info, font=("Arial", 12), justify=ctk.LEFT)
        label.pack(side=ctk.LEFT, padx=10)

        buy_button = ctk.CTkButton(self.search_result_frame, text="Купити",
                                   command=lambda p=product: self.add_to_cart(p))
        buy_button.pack(side=ctk.RIGHT, padx=10)
root = ctk.CTk()
app = OnlineStoreApp(root)
root.mainloop()

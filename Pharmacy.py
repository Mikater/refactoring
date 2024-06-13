import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import time


class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("~ Ап+те+Ка ~")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        self.menu_frame = ctk.CTkFrame(self.root)
        self.menu_frame.pack(side=ctk.TOP, fill=ctk.X)

        self.search_entry = ctk.CTkEntry(self.menu_frame, placeholder_text="Пошук...")
        self.search_entry.pack(side=ctk.LEFT, padx=10)

        self.search_button = ctk.CTkButton(self.menu_frame, text="+ Пошук +", command=self.search_medicine)
        self.search_button.pack(side=ctk.LEFT, padx=10)
        self.last_searched_medicine = None

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        self.create_menu()
        self.create_main_interface()

        self.time_label = ctk.CTkLabel(root, text="", font=('Helvetica', 12))
        self.time_label.pack(side=ctk.BOTTOM, anchor='se', pady=10, padx=10)
        self.update_clock()

        self.show_menu()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S\n%D')
        self.time_label.configure(text=current_time)
        self.root.after(1000, self.update_clock)

    def create_menu(self):
        ctk.CTkButton(self.menu_frame, text="+ Меню +", command=self.show_menu).pack(side=ctk.LEFT)
        ctk.CTkButton(self.menu_frame, text="+ Кошик +", command=self.show_cart).pack(side=ctk.LEFT)

    def create_main_interface(self):
        self.medicines = [
            {"name": "Аспірин", "price": 70, "description": "Для полегшення болю та покращення самопочуття."},
            {"name": "Парацетамол", "price": 25, "description": "Ліки від болю та підвищення температури."},
            {"name": "Но-шпа", "price": 100, "description": "Для зняття судом та спазмів кишечнику."},
            {"name": "Феністил", "price": 160, "description": "Антигістамінний засіб для лікування алергійних захворювань."},
            {"name": "Амоксил", "price": 185, "description": "Антибіотик для лікування інфекційних захворювань."},
            {"name": "Лізак", "price": 145, "description": "Для лікування захворювань ротової порожнини."},
            {"name": "Ібупрофен", "price": 60, "description": "Протизапальний засіб для зняття болю та зниження температури."},
            {"name": "Нурофен", "price": 160, "description": "Обезболюючий припарат при менструальних болях, шлункових полях, спазмових болях."},
            {"name": "Цитрамон", "price": 20, "description": "Комбінований препарат для полегшення головного болю та зниження температури."},
            {"name": "Ентеросгель", "price": 70, "description": "Сорбент для очищення організму від токсинів та алергенів."},
            {"name": "Карсил", "price": 245, "description": "Гепатопротектор для захисту та відновлення печінки."}
        ]

        self.cart = []

    def show_menu(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.main_frame, text="~+~ Cписок Ліків ~+~", font=("Arial", 14)).pack(pady=10)
        for medicine in self.medicines:
            self.add_medicine_to_frame(medicine)

    def add_medicine_to_frame(self, medicine):
        frame = ctk.CTkFrame(self.main_frame)
        frame.pack(fill=ctk.X, pady=5)

        medicine_info = f"{medicine['name']} - {medicine['price']} грн"
        label = ctk.CTkLabel(frame, text=medicine_info, font=("Arial", 12), justify=ctk.LEFT)
        label.pack(side=ctk.LEFT, padx=10)

        add_button = ctk.CTkButton(frame, text="Додати до кошика", command=lambda m=medicine: self.add_to_cart(m))
        add_button.pack(side=ctk.RIGHT, padx=10)

    def add_to_cart(self, medicine):
        self.cart.append(medicine)
        CTkMessagebox(title="Кошик", message=f"{medicine['name']} додано до кошика", icon="check")

    def show_cart(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.main_frame, text="<=> Ваш Кошик <=>", font=("Arial", 14)).pack(pady=10)

        total_price = sum(medicine['price'] for medicine in self.cart)
        for index, medicine in enumerate(self.cart):
            medicine_info = f"{medicine['name']} - ціна {medicine['price']} грн"
            frame = ctk.CTkFrame(self.main_frame)
            frame.pack(fill=ctk.X, pady=5)
            frame = ctk.CTkFrame(self.main_frame)
            frame.pack(fill=ctk.X, pady=5)

            label = ctk.CTkLabel(frame, text=medicine_info, font=("Arial", 12), justify=ctk.LEFT)
            label.pack(side=ctk.LEFT, padx=10)

            delete_button = ctk.CTkButton(frame, text="❌", fg_color="red", width=10,
                                          command=lambda idx=index: self.remove_from_cart(idx))
            delete_button.pack(side=ctk.RIGHT, padx=5)

        total_label = ctk.CTkLabel(self.main_frame, text=f"Загальна вартість: {total_price} грн", font=("Arial", 14))
        total_label.pack(pady=10)

    def remove_from_cart(self, index):
        del self.cart[index]
        self.show_cart()

    def search_medicine(self):
        search_term = self.search_entry.get()
        if not search_term:
            CTkMessagebox(title="Пошук", message="Пошук пустий.", icon="cancel")
            return

        for medicine in self.medicines:
            if search_term.lower() in medicine['name'].lower():
                self.display_search_result(medicine)
                return

        CTkMessagebox(title="Пошук", message="Лікарський засіб не знайдено.", icon="cancel")

    def display_search_result(self, medicine):
        if hasattr(self, 'search_result_frame'):
            self.search_result_frame.destroy()

        self.search_result_frame = ctk.CTkFrame(self.root)
        self.search_result_frame.pack(side=ctk.TOP, fill=ctk.X, padx=10, pady=5)

        medicine_info = f"{medicine['name']} - {medicine['price']} грн\n{medicine['description']}"
        label = ctk.CTkLabel(self.search_result_frame, text=medicine_info, font=("Arial", 12), justify=ctk.LEFT)
        label.pack(side=ctk.LEFT, padx=10)

        buy_button = ctk.CTkButton(self.search_result_frame, text="Купити",
                                   command=lambda m=medicine: self.add_to_cart(m))
        buy_button.pack(side=ctk.RIGHT, padx=10)

root = ctk.CTk()
app = PharmacyApp(root)
root.mainloop()
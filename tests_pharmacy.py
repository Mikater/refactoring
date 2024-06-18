# Тестовий файл: test_pharmacy.py

import unittest
import customtkinter as ctk
from Pharmacy import PharmacyApp
import time


class TestPharmacyApp(unittest.TestCase):

    def setUp(self):
        self.root = ctk.CTk()
        self.app = PharmacyApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_init(self):
        self.assertEqual(self.app.root.title(), "~ Ап+те+Ка ~")
        self.assertEqual(self.app.root.geometry(), "900x600")

    def test_create_menu(self):
        self.assertEqual(len(self.app.menu_frame.winfo_children()), 2)

    def test_create_main_interface(self):
        self.assertEqual(len(self.app.medicines), 11)

    def test_show_menu(self):
        self.app.show_menu()
        self.assertEqual(len(self.app.main_frame.winfo_children()), 12)

    def test_add_medicine_to_frame(self):
        self.app.show_menu()
        medicine = self.app.medicines[0]
        self.app.add_medicine_to_frame(medicine)
        self.assertEqual(len(self.app.main_frame.winfo_children()), 13)

    def test_add_to_cart(self):
        medicine = self.app.medicines[0]
        self.app.add_to_cart(medicine)
        self.assertEqual(len(self.app.cart), 1)
        self.assertEqual(self.app.cart[0], medicine)

    def test_show_cart(self):
        self.app.add_to_cart(self.app.medicines[0])
        self.app.show_cart()
        self.assertEqual(len(self.app.main_frame.winfo_children()), 3)

    def test_remove_from_cart(self):
        self.app.add_to_cart(self.app.medicines[0])
        self.app.remove_from_cart(0)
        self.assertEqual(len(self.app.cart), 0)

    def test_search_medicine(self):
        self.app.search_entry.insert(0, "Аспірин")
        self.app.search_medicine()
        self.assertTrue(hasattr(self.app, 'search_result_frame'))
        self.assertEqual(self.app.search_result_frame.winfo_children()[0].cget("text"),
                         "Аспірин - 70 грн\nДля полегшення болю та покращення самопочуття.")

    def test_search_medicine_not_found(self):
        self.app.search_entry.insert(0, "Unknown")
        self.app.search_medicine()
        self.assertFalse(hasattr(self.app, 'search_result_frame'))

    def test_display_search_result(self):
        self.app.display_search_result(self.app.medicines[0])
        self.assertTrue(hasattr(self.app, 'search_result_frame'))
        self.assertEqual(self.app.search_result_frame.winfo_children()[0].cget("text"),
                         "Аспірин - 70 грн\nДля полегшення болю та покращення самопочуття.")

    def test_update_clock(self):
        self.app.update_clock()
        current_time = time.strftime('%H:%M:%S\n%D')
        self.assertEqual(self.app.time_label.cget("text"), current_time)

    def test_cart_total_price(self):
        self.app.add_to_cart(self.app.medicines[0])
        self.app.add_to_cart(self.app.medicines[1])
        total_price = sum(medicine['price'] for medicine in self.app.cart)
        self.assertEqual(total_price, 95)

    def test_add_to_cart_multiple(self):
        self.app.add_to_cart(self.app.medicines[0])
        self.app.add_to_cart(self.app.medicines[1])
        self.assertEqual(len(self.app.cart), 2)
        self.assertEqual(self.app.cart[0], self.app.medicines[0])
        self.assertEqual(self.app.cart[1], self.app.medicines[1])

    def test_menu_buttons_exist(self):
        self.assertEqual(self.app.menu_frame.winfo_children()[0].cget("text"), "+ Меню +")
        self.assertEqual(self.app.menu_frame.winfo_children()[1].cget("text"), "+ Кошик +")

    def test_empty_cart(self):
        self.app.show_cart()
        total_price = sum(medicine['price'] for medicine in self.app.cart)
        self.assertEqual(total_price, 0)

    def test_cart_delete_button(self):
        self.app.add_to_cart(self.app.medicines[0])
        self.app.show_cart()
        delete_button = self.app.main_frame.winfo_children()[1].winfo_children()[1]
        delete_button.invoke()
        self.assertEqual(len(self.app.cart), 0)

    def test_search_empty_entry(self):
        self.app.search_medicine()
        self.assertFalse(hasattr(self.app, 'search_result_frame'))

    def test_add_and_remove_cart(self):
        self.app.add_to_cart(self.app.medicines[0])
        self.app.remove_from_cart(0)
        self.assertEqual(len(self.app.cart), 0)

    def test_clock_update_continuous(self):
        initial_time = self.app.time_label.cget("text")
        time.sleep(2)
        updated_time = self.app.time_label.cget("text")
        self.assertNotEqual(initial_time, updated_time)


if __name__ == "__main__":
    unittest.main()

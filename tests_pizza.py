import unittest
from unittest.mock import patch, MagicMock
import customtkinter as ctk
from tkinter import Toplevel
from CTkMessagebox import CTkMessagebox
from Pizza import OnlineStoreApp  # Ваш файл з кодом

class TestOnlineStoreApp(unittest.TestCase):
    def setUp(self):
        self.root = ctk.CTk()
        self.app = OnlineStoreApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_title(self):
        self.assertEqual(self.app.root.title(), "Онлайн Магазин")

    def test_initial_geometry(self):
        self.assertEqual(self.app.root.geometry(), "900x600")

    def test_search_button_initial_state(self):
        self.assertEqual(self.app.search_button.cget("text"), "Пошук")

    def test_initial_switch_var(self):
        self.assertEqual(self.app.switch_var.get(), "off")

    @patch('time.strftime', return_value='12:34:56\n01/01/23')
    def test_update_clock(self, mock_time):
        self.app.update_clock()
        self.assertEqual(self.app.time_label.cget("text"), "12:34:56\n01/01/23")

    def test_create_menu_buttons(self):
        buttons = self.app.menu_frame.winfo_children()
        self.assertEqual(buttons[0].cget("text"), "Меню")
        self.assertEqual(buttons[1].cget("text"), "Замовлення")
        self.assertEqual(buttons[2].cget("text"), "Кошик")

    def test_switch_event_dark_mode(self):
        self.app.switch_var.set('on')
        self.app.switch_event()
        self.assertEqual(ctk.get_appearance_mode(), "light")

    def test_switch_event_light_mode(self):
        self.app.switch_var.set('off')
        self.app.switch_event()
        self.assertEqual(ctk.get_appearance_mode(), "dark")

    def test_product_base_initial_products(self):
        self.assertGreater(len(self.app.products), 0)

    def test_product_base_initial_ingridients(self):
        self.assertGreater(len(self.app.ingridient), 0)

    def test_show_menu_creates_main_frame(self):
        self.app.show_menu()
        self.assertTrue(self.app.main_frame.winfo_exists())

    def test_show_orders_creates_main_frame(self):
        self.app.show_orders()
        self.assertTrue(self.app.main_frame.winfo_exists())

    def test_create_custom_pizza_creates_window(self):
        with patch('tkinter.Toplevel') as mock_toplevel:
            self.app.create_custom_pizza()
            self.assertTrue(mock_toplevel.called)

    def test_create_custom_set_creates_window(self):
        with patch('tkinter.Toplevel') as mock_toplevel:
            self.app.create_custom_set()
            self.assertTrue(mock_toplevel.called)

    def test_show_cart_creates_main_frame(self):
        self.app.show_cart()
        self.assertTrue(self.app.main_frame.winfo_exists())

    def test_add_product_to_cart(self):
        initial_cart_size = len(self.app.cart)
        product = self.app.products[0]
        self.app.add_to_cart(product)
        self.assertEqual(len(self.app.cart), initial_cart_size + 1)
        self.assertEqual(self.app.cart[-1], product)

    def test_search_product_not_found(self):
        self.app.search_entry.insert(0, "Невідомий продукт")
        with patch('CTkMessagebox.showinfo') as mock_messagebox:
            self.app.search_product()
            mock_messagebox.assert_called_with(title="Пошук", message="Продукт не знайдено.", icon="cancel")

    def test_search_product_found(self):
        self.app.search_entry.insert(0, "Піца Грибна")
        with patch.object(self.app, 'display_search_result') as mock_display:
            self.app.search_product()
            mock_display.assert_called()

    def test_display_search_result_creates_frame(self):
        product = self.app.products[0]
        self.app.display_search_result(product)
        self.assertTrue(self.app.search_result_frame.winfo_exists())

if __name__ == "__main__":
    unittest.main()

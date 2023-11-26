from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class ProductScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="Product Name:"))
        self.product_name_input = TextInput(multiline=False)
        self.add_widget(self.product_name_input)

        self.add_widget(Label(text="Product Stock:"))
        self.product_stock_input = TextInput(multiline=False, input_type='number')
        self.add_widget(self.product_stock_input)

        self.add_widget(Label(text="Product Price:"))
        self.product_price_input = TextInput(multiline=False, input_type='number')
        self.add_widget(self.product_price_input)

        self.add_product_btn = Button(text="Add Product")
        self.add_product_btn.bind(on_press=self.add_product)
        self.add_widget(self.add_product_btn)

        self.search_product_btn = Button(text="Search Product by ID")
        self.search_product_btn.bind(on_press=self.search_product)
        self.add_widget(self.search_product_btn)

        self.view_products_btn = Button(text="View All Products")
        self.view_products_btn.bind(on_press=self.view_products)
        self.add_widget(self.view_products_btn)

        self.product_list = []
        self.product_id = 0

    def add_product(self, instance):
        name = self.product_name_input.text
        stock = self.product_stock_input.text
        price = self.product_price_input.text
        self.product_id += 1
        product = {
            "ID": self.product_id,
            "Name": name,
            "Stock": stock,
            "Price": price
        }
        self.product_list.append(product)
        self.show_popup("Product Added", f"Added {name} with ID {self.product_id}")

    def search_product(self, instance):
        search_id = int(self.product_name_input.text)  # Assuming using product name input for ID search
        found_product = next((product for product in self.product_list if product["ID"] == search_id), None)
        if found_product:
            self.show_popup("Product Found", f"Product: {found_product}")
        else:
            self.show_popup("Product Not Found", "No product with this ID")

    def view_products(self, instance):
        product_details = '\n'.join(str(product) for product in self.product_list)
        self.show_popup("All Products", product_details if product_details else "No products available")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 400))
        popup.open()

class InventoryApp(App):
    def build(self):
        return ProductScreen()

if __name__ == '__main__':
    InventoryApp().run()

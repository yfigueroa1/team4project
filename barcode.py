from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class BarcodeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="Enter Barcode:"))
        self.barcode_input = TextInput(multiline=False)
        self.add_widget(self.barcode_input)

        self.add_widget(Label(text="Enter Quantity:"))
        self.quantity_input = TextInput(multiline=False, input_type='number')
        self.add_widget(self.quantity_input)

        self.add_item_btn = Button(text="Add Item")
        self.add_item_btn.bind(on_press=self.add_item)
        self.add_widget(self.add_item_btn)

        self.remove_item_btn = Button(text="Remove Item")
        self.remove_item_btn.bind(on_press=self.remove_item)
        self.add_widget(self.remove_item_btn)

        self.show_inventory_btn = Button(text="Show Inventory")
        self.show_inventory_btn.bind(on_press=self.show_inventory)
        self.add_widget(self.show_inventory_btn)

        self.inventory = {}

    def add_item(self, instance):
        barcode = self.barcode_input.text
        try:
            quantity = int(self.quantity_input.text)
        except ValueError:
            self.show_popup("Error", "Invalid quantity")
            return

        if barcode in self.inventory:
            self.inventory[barcode] += quantity
        else:
            self.inventory[barcode] = quantity
        self.show_popup("Success", f"Added {quantity} item(s) with barcode {barcode}")

    def remove_item(self, instance):
        barcode = self.barcode_input.text
        try:
            quantity = int(self.quantity_input.text)
        except ValueError:
            self.show_popup("Error", "Invalid quantity")
            return

        if barcode in self.inventory and self.inventory[barcode] >= quantity:
            self.inventory[barcode] -= quantity
            if self.inventory[barcode] == 0:
                del self.inventory[barcode]
            self.show_popup("Success", f"Removed {quantity} item(s) with barcode {barcode}")
        else:
            self.show_popup("Error", "Not enough items or barcode not found")

    def show_inventory(self, instance):
        inventory_str = "\n".join(f"Barcode: {barcode}, Count: {count}" for barcode, count in self.inventory.items())
        self.show_popup("Current Inventory", inventory_str if inventory_str else "Inventory is empty")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 400))
        popup.open()

class InventoryApp(App):
    def build(self):
        return BarcodeScreen()

if __name__ == '__main__':
    InventoryApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import StringProperty

class InventoryItem(RecycleDataViewBehavior, BoxLayout):
    item_id = StringProperty()
    item_name = StringProperty()
    quantity = StringProperty()

class InventoryList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []

class QuantityPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.inventory = {'item1': {'name': 'Item 1', 'quantity': 10}, 
                          'item2': {'name': 'Item 2', 'quantity': 5}, 
                          'item3': {'name': 'Item 3', 'quantity': 15}}

        self.add_widget(Label(text="Inventory Management App", font_size='20sp'))

        self.inventory_list = InventoryList()
        self.add_widget(self.inventory_list)
        self.populate_inventory()

        self.add_widget(Label(text="Enter new quantity:"))
        self.quantity_entry = TextInput(multiline=False, input_type='number')
        self.add_widget(self.quantity_entry)

        self.update_quantity_btn = Button(text="Update Quantity")
        self.update_quantity_btn.bind(on_press=self.update_quantity)
        self.add_widget(self.update_quantity_btn)

    def populate_inventory(self):
        self.inventory_list.data = [{'item_id': item_id, 'item_name': details['name'], 'quantity': str(details['quantity'])}
                                    for item_id, details in self.inventory.items()]

    def update_quantity(self, instance):
        if not self.inventory_list.layout_manager.selected_nodes:
            self.show_popup("Warning", "Please select an item from the inventory.")
            return

        selected_index = self.inventory_list.layout_manager.selected_nodes[0]
        selected_item_id = self.inventory_list.data[selected_index]['item_id']

        new_quantity = self.quantity_entry.text
        try:
            new_quantity = int(new_quantity)
            if new_quantity < 0:
                raise ValueError("Quantity cannot be negative.")
        except ValueError as e:
            self.show_popup("Error", f"Invalid quantity: {e}")
            return

        self.inventory[selected_item_id]['quantity'] = new_quantity
        self.inventory_list.data[selected_index]['quantity'] = str(new_quantity)
        self.show_popup("Success", "Quantity updated successfully.")
        self.quantity_entry.text = ''

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 400))
        popup.open()

class InventoryApp(App):
    def build(self):
        return QuantityPage()

if __name__ == '__main__':
    InventoryApp().run()

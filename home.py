from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="Welcome to Inventory Management", font_size='20sp'))

        self.button_new_item = Button(text="New Item")
        self.button_new_item.bind(on_press=self.open_new_item_window)
        self.add_widget(self.button_new_item)

        self.button_view_inventory = Button(text="View Inventory")
        self.button_view_inventory.bind(on_press=self.open_view_inventory_window)
        self.add_widget(self.button_view_inventory)

        self.button_exit = Button(text="Exit")
        self.button_exit.bind(on_press=self.exit_app)
        self.add_widget(self.button_exit)

    def open_new_item_window(self, instance):
        print("Opening New Item Window")
        # Here, you would actually switch to a different screen or pop up a new window

    def open_view_inventory_window(self, instance):
        print("Opening View Inventory Window")
        # Similar to above, switch to the relevant screen

    def exit_app(self, instance):
        App.get_running_app().stop()

class InventoryApp(App):
    def build(self):
        return HomePage()

if __name__ == '__main__':
    Invent

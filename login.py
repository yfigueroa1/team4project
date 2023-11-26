from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login_btn = Button(text='Login')
        self.login_btn.bind(on_press=self.validate_credentials)
        self.add_widget(self.login_btn)

    def validate_credentials(self, instance):
        valid_credentials = {"admin": "password123"}
        if valid_credentials.get(self.username.text) == self.password.text:
            popup = Popup(title='Login Successful',
                          content=Label(text=f'Welcome, {self.username.text}!'),
                          size_hint=(None, None), size=(200, 200))
        else:
            popup = Popup(title='Login Failed',
                          content=Label(text='Invalid username or password'),
                          size_hint=(None, None), size=(200, 200))
        popup.open()

class InventoryApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    InventoryApp().run()

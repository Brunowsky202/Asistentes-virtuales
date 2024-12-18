from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class tablita(GridLayout):
    name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    food = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(tablita, self).__init__(**kwargs)

        
        print(self.name.text)
    
    def press(self):
        name = self.name.text
        food = self.food.text
        last_name = self.last_name.text

        imprimir = (f"hola {name} {last_name}, tu comida favorita es {food}")
        self.add_widget(Label(text = imprimir ))

        self.name.text = ""
        self.last_name.text = ""
        self.food.text = ""

class PongApp(App):
    def build(self):
        return tablita()
    
PongApp().run()


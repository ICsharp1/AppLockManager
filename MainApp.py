from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from numpy import spacing
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget


BlueBackground = (71, 161, 221, 0)
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

RESOURCEPATH = 'C:\\Users\\israe\\OneDrive\\שולחן העבודה\\\AppLockManager\\Resources\\'
LAYOUTS = 'C:\\Users\\israe\\OneDrive\\שולחן העבודה\\\AppLockManager\\Layouts\\'

Builder.load_file(LAYOUTS + 'Button.kv')
Builder.load_file(LAYOUTS + 'whatever.kv')


Window.size = (400, 600)
Window.clearcolor = BlueBackground


class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=100, spacing=5)
        colors = [red, green, blue, purple]

        btn = Button(text='Click Me!',
                     size_hint=(.5, .5),
                     pos_hint={'center_x': .5, 'center_y': .5})
        btn.bind(on_press=self.on_press_button)

        layout.add_widget(btn)
        return layout

    def on_press_button(self, instance):
        print("You clicked the button " + instance.text)


class MainApp(App):
    def build(self):
        return whatever_two()

    def on_press_button(self, instance):
        print("You clicked the button " + instance.text)


class whatever_two(Widget):

    def on_press_button(self, instance):
        print("You clicked the button " + instance.text)


if __name__ == "__main__":

    app = MainApp()
    app.run()

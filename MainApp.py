from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

RESOURCEPATH = 'C:\\Users\\israe\\OneDrive\\שולחן העבודה\\\AppLockManager\\Resources\\'


class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy (#IC)',
                      size_hint=(1, .5),
                      pos_hint={'center_x': 0.18, 'center_y': 0.965})
        label.font_size = '30sp'

        img = Image(source=RESOURCEPATH + 'KivyImage.jpg',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})
        return label


if __name__ == "__main__":
    app = MainApp()
    app.run()

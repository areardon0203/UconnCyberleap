import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image 
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        testBtn = Button(size = (500,500), text = "Hello World!",
            background_normal = 'LeeLee.png')
        return testBtn    

root=ButtonApp()  
root.run()

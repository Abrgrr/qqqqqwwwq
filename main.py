from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics','resizable','0')
Config.set('graphics','width','1000')
Config.set('graphics','height','500')
c=1
class myApp(App):
    def build(self):
        return Button(text='нажми на кнопку',
                      font_size=40,
                      background_color=[.32, .85, .94,1] ,
                      on_press=self.press_button,
                      background_normal='')
    def press_button(self, instance):
        global c
        c+=1
        #print(c)
        #print(c)
        instance.background_color=[.32, .85, .94,1]
        instance.text=str(c)
if __name__ == '__main__':
    myApp().run()


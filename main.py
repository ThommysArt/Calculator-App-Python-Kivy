# Importing Required modules
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.config import Config
from kivy import properties as p
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.menu import MDDropdownMenu
from sympy import Symbol
import time
import darkdetect

# Importing local modules
from libs.Diff_integr import diffr, integr
from libs.evaluate import evaluation, fact, trig_fxn, modulo
from libs.currency_converter import converter
from libs.volume_converter import to_milimeter, milimeter_to, volconvert
from libs.length_converter import to_microns, microns_to, lenconvert
from libs.mass_converter import to_miligrams, miligrams_to, mass_convert

# Importing Screens
from Screens.StandardScreen import StandardScreen
from Screens.CurrencyScreen import CurrencyScreen
from Screens.LengthScreen import LengthScreen
from Screens.ScientificScreen import ScientificScreen
from Screens.VolumeScreen import VolumeScreen
from Screens.WeightMassScreen import Weight_MassScreen

class MyLabel(MDLabel):
    pass


class SwitchScreen(MDScreenManager):
    pass
      

# App class
class CalculatorApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.uix = Builder.load_file('my.kv')
        menu_items = [
            {
                "text": "Standard",
                "height": dp(54),
                "left_icon": "calculator",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="standard": self.switch_screen(x),
            },
            {
                "text": "Scientific",
                "height": dp(54),
                "left_icon": "flask",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="scientific": self.switch_screen(x),
            },
            {
                "text": "Currency",
                "height": dp(54),
                "left_icon": "currency-usd",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="currency": self.switch_screen(x),
            },
            {
                "text": "Volume",
                "height": dp(54),
                "left_icon": "cube",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="volume": self.switch_screen(x),
            },
            {
                "text": "Length",
                "height": dp(54),
                "left_icon": "ruler",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="length": self.switch_screen(x),
            },
            {
                "text": "Weight & Mass",
                "height": dp(54),
                "left_icon": "weight",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="weight": self.switch_screen(x),
            },
            
        ]
        self.menu = MDDropdownMenu(
            caller=StandardScreen().ids.topbar,
            items=menu_items,
            width_mult=4
        )


    def build(self):
        
        Window.size = (400, 540)
        Config.set("kivy", "window_icon", "475497.png")
        if darkdetect.isDark():
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
        self.icon = "475497.png"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return SwitchScreen()
    
    def change_theme(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            MyLabel().text_color = 0,0,0,1
        else:
            self.theme_cls.theme_style = "Dark"
            MyLabel().text_color = 1,1,1,1
        
    def switch_screen(self, screen):
        self.root.current = screen
    


if __name__ == "__main__":
    CalculatorApp().run()
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


from .StandardScreen import StandardScreen



# Length page class
class LengthScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menu_items = [
            {
            "text": f"{leng}",
            "viewclass": "OneLineListItem",
            "on_release": lambda x=f"{leng}": self.set_length1(x)
            } for leng in microns_to
        ]
            
        self.menu = MDDropdownMenu(
            caller=StandardScreen().ids.topbar,
            items=menu_items,
            width_mult=4
        )

        menu_items2 = [
            {
            "text": f"{leng}",
            "viewclass": "OneLineListItem",
            "on_release": lambda x=f"{leng}": self.set_length2(x)
            } for leng in to_microns
        ]
        
        self.menu2 = MDDropdownMenu(
            caller=StandardScreen().ids.topbar,
            items=menu_items2,
            width_mult=4
        )

    def erase(self):
        expr = str(self.ids.text_bar.text)
        expr = expr[:len(expr)-1]
        self.ids.text_bar.text = expr


    def set_length1(self, leng1):
        self.ids.text_bar.hint_text = f"In {leng1}"
        self.ids.first_leng.text = str(leng1)

    def set_length2(self, leng2):
        self.ids.result_bar.hint_text = f"In {leng2}"
        self.ids.second_leng.text = str(leng2)

    def length_convert(self):
        leng1 = str(self.ids.first_leng.text)
        leng2 = str(self.ids.second_leng.text)
        amount = float(self.ids.text_bar.text)
        self.ids.result_bar.text = str(lenconvert(leng1,leng2,amount))

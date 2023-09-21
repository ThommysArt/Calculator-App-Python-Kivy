from .StandardScreen import StandardScreen

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



class Weight_MassScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menu_items = [
            {
            "text": f"{mass}",
            "viewclass": "OneLineListItem",
            "on_release": lambda x=f"{mass}": self.set_mass1(x)
            } for mass in miligrams_to
        ]
            
        self.menu = MDDropdownMenu(
            caller=StandardScreen().ids.topbar,
            items=menu_items,
            width_mult=4
        )

        menu_items2 = [
            {
            "text": f"{mass}",
            "viewclass": "OneLineListItem",
            "on_release": lambda x=f"{mass}": self.set_mass2(x)
            } for mass in to_miligrams
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


    def set_mass1(self, mass1):
        self.ids.text_bar.hint_text = f"In {mass1}"
        self.ids.first_mass.text = str(mass1)

    def set_mass2(self, mass2):
        self.ids.result_bar.hint_text = f"In {mass2}"
        self.ids.second_mass.text = str(mass2)

    def weight_convert(self):
        mass1 = str(self.ids.first_mass.text)
        mass2 = str(self.ids.second_mass.text)
        amount = float(self.ids.text_bar.text)
        self.ids.result_bar.text = str(mass_convert(mass1,mass2,amount))

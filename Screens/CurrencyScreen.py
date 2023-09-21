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


#Currency class
class CurrencyScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menu_items = [
            {
                "text": "USD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="USD": self.change_curr1(x),
            },
            {
                "text": "CAD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CAD": self.change_curr1(x),
            },
            {
                "text": "EUR",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="EUR": self.change_curr1(x),
            },
            {
                "text": "XAF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="XAF": self.change_curr1(x),
            },
            {
                "text": "GBP",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="GBP": self.change_curr1(x),
            },
            {
                "text": "JPY",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="JPY": self.change_curr1(x),
            },
            {
                "text": "AUD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="AUD": self.change_curr1(x),
            },
            {
                "text": "CHF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CHF": self.change_curr1(x),
            },
            {
                "text": "ZAR",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="ZAR": self.change_curr1(x),
            },
            {
                "text": "SEK",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="SEK": self.change_curr1(x),
            },
            {
                "text": "CNY",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CNY": self.change_curr1(x),
            },
            {
                "text": "CDF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CDF": self.change_curr1(x),
            },
            {
                "text": "EGP",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="EGP": self.change_curr1(x),
            },
            {
                "text": "ETB",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="ETB": self.change_curr1(x),
            },
            {
                "text": "GHS",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="GHS": self.change_curr1(x),
            },
            {
                "text": "VND",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="VND": self.change_curr1(x),
            },
            {
                "text": "INR",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="INR": self.change_curr1(x),
            },
            {
                "text": "CHF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CHF": self.change_curr1(x),
            },
            {
                "text": "KES",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="KES": self.change_curr1(x),
            },
            {
                "text": "KRW",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="KRW": self.change_curr1(x),
            },
            {
                "text": "KWD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="KWD": self.change_curr1(x),
            },
            {
                "text": "MXN",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="MXN": self.change_curr1(x),
            },
            {
                "text": "NGN",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="NGN": self.change_curr1(x),
            },
            {
                "text": "AED",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="AED": self.change_curr1(x),
            }
        ]

        menu_items2 = [
            {
                "text": "USD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="USD": self.change_curr2(x),
            },
            {
                "text": "CAD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CAD": self.change_curr2(x),
            },
            {
                "text": "EUR",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="EUR": self.change_curr2(x),
            },
            {
                "text": "XAF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="XAF": self.change_curr2(x),
            },
            {
                "text": "GBP",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="GBP": self.change_curr2(x),
            },
            {
                "text": "JPY",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="JPY": self.change_curr2(x),
            },
            {
                "text": "AUD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="AUD": self.change_curr2(x),
            },
            {
                "text": "CHF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CHF": self.change_curr2(x),
            },
            {
                "text": "ZAR",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="ZAR": self.change_curr2(x),
            },
            {
                "text": "SEK",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="SEK": self.change_curr2(x),
            },
            {
                "text": "CNY",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CNY": self.change_curr2(x),
            },
            {
                "text": "CDF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CDF": self.change_curr2(x),
            },
            {
                "text": "EGP",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="EGP": self.change_curr2(x),
            },
            {
                "text": "ETB",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="ETB": self.change_curr2(x),
            },
            {
                "text": "GHS",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="GHS": self.change_curr2(x),
            },
            {
                "text": "VND",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="VND": self.change_curr2(x),
            },
            {
                "text": "INR",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="INR": self.change_curr2(x),
            },
            {
                "text": "CHF",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="CHF": self.change_curr2(x),
            },
            {
                "text": "KES",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="KES": self.change_curr2(x),
            },
            {
                "text": "KRW",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="KRW": self.change_curr2(x),
            },
            {
                "text": "KWD",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="KWD": self.change_curr2(x),
            },
            {
                "text": "MXN",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="MXN": self.change_curr2(x),
            },
            {
                "text": "NGN",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="NGN": self.change_curr2(x),
            },
            {
                "text": "AED",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="AED": self.change_curr2(x),
            }
        ]

        self.menu1 = MDDropdownMenu(
            caller=StandardScreen().ids.topbar,
            items=menu_items,
            width_mult=2
        )

        self.menu2 = MDDropdownMenu(
            caller=StandardScreen().ids.topbar,
            items=menu_items2,
            width_mult=2
        )
    
    def erase(self):
        expr = str(self.ids.text_bar.text)
        expr = expr[:len(expr)-1]
        self.ids.text_bar.text = expr


    def change_curr1(self, curr1):
        self.ids.text_bar.hint_text = f"In {curr1}"
        self.ids.first_curr.text = str(curr1)

    def change_curr2(self, curr2):
        self.ids.result_bar.hint_text = f"In {curr2}"
        self.ids.second_curr.text = str(curr2)

    def convert_curr(self):
        curr1 = str(self.ids.first_curr.text)
        curr2 = str(self.ids.second_curr.text)
        amount = self.ids.text_bar.text
        self.ids.result_bar.text = str(converter(curr1, curr2, float(amount)))

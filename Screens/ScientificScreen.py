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

#Scientific class
class ScientificScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menu_items = [
            {
                "text": "cos",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="cos": self.trig_function(x),
            },
            {
                "text": "sin",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="sin": self.trig_function(x),
            },
            {
                "text": "tan",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="tan": self.trig_function(x),
            },
            {
                "text": "cosh",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="cosh": self.trig_function(x),
            },
            {
                "text": "sinh",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="sinh": self.trig_function(x),
            },
            {
                "text": "tanh",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="tanh": self.trig_function(x),
            },
            {
                "text": "acos",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="acos": self.trig_function(x),
            },
            {
                "text": "asin",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="asin": self.trig_function(x),
            },
            {
                "text": "atan",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="atan": self.trig_function(x),
            },
            {
                "text": "acosh",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="acosh": self.trig_function(x),
            },
            {
                "text": "asinh",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="asinh": self.trig_function(x),
            },
            {
                "text": "atanh",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="atanh": self.trig_function(x),
            }
        ]
        self.menu = MDDropdownMenu(
            caller=StandardScreen().ids.topbar,
            items=menu_items,
            width_mult=2
        )

    def sign(self):
        expr = "-1*" + str(self.ids.text_bar.text)
        self.ids.text_bar.text = str(evaluation(expr))

    def erase(self):
        expr = str(self.ids.text_bar.text)
        expr = expr[:len(expr)-1]
        self.ids.text_bar.text = expr


    def evaluate(self):
        expr = self.ids.text_bar.hint_text
        self.ids.text_bar.text = str(evaluation(expr))

   
    def convert(self, curr1, curr2, amount):
        curr1 = self.ids.text_bar.hint_text
        curr2 = self.ids.text_bar.helper_text
        amount = self.ids.text_bar.text
        self.ids.text_bar.text = str(converter(curr1, curr2, int(amount)))

    def mod(self):
        expr = str(self.ids.text_bar.text)
        self.ids.text_bar.hint_text += self.ids.text_bar.text + "mod(10)"
        self.ids.text_bar.text = str(modulo(expr,10))
    
    def exp(self):
        exp = 10
        expr = str(self.ids.text_bar.text)
        self.ids.text_bar.hint_text = expr + ".e+"+ str(exp)
        self.ids.text_bar.text = str(expr)
        for i in range(int(exp)):
            self.ids.text_bar.text += '0'

    def differentiate(self):
        expr = str(self.ids.text_bar.text)
        self.ids.text_bar.hint_text = "d(" + self.ids.text_bar.text + ")/dx"
        x = Symbol('x')
        self.ids.text_bar.text = str(diffr(expr, x))
        
    def Integrate(self):
        expr = str(self.ids.text_bar.text)
        self.ids.text_bar.hint_text = "|(" + self.ids.text_bar.text + ")dx"
        self.ids.text_bar.text = str(integr(expr))

    def trig_function(self, trig):
        try:
            expr = float(self.ids.text_bar.text)
            self.ids.text_bar.hint_text = trig + "(" + self.ids.text_bar.text + ")"
            self.ids.text_bar.text = str(trig_fxn(trig, expr))
        except:
            self.ids.text_bar.text = "Math Error"

    def nfactorial(self):
        n = int(self.ids.text_bar.text)
        self.ids.text_bar.hint_text = str(n) + "!"
        self.ids.text_bar.text = str(fact(n))
   
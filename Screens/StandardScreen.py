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

class StandardScreen(MDScreen):

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

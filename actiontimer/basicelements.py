from __future__ import print_function

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.base import runTouchApp
from kivy.uix.button import Button, Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.bubble import Bubble
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock

import actiontimer


class IntervallInput(BoxLayout):
    number = StringProperty("0")
    def __init__(self, **kwargs):
        super(IntervallInput, self).__init__(**kwargs)
    
    def one_up(self):
        self.number = str(int(self.number)+1)
        #print( self.number)
        
    def one_down(self):
        
        value=int(self.number)-1
        if not value < 0:
            self.number = str(value)
        #print( self.number)
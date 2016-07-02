from __future__ import print_function

from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.properties import StringProperty

#from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
#from kivy.base import runTouchApp
#from kivy.uix.button import Button, Label
#from kivy.uix.popup import Popup
#from kivy.uix.scrollview import ScrollView
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.behaviors.focus import FocusBehavior
#from kivy.properties import BooleanProperty, NumericProperty, ObjectProperty
#from kivy.event import EventDispatcher

from kivy.clock import Clock

from kivy.core.audio import SoundLoader

import actiontimer

Builder.load_file('actiontimer/kv/basicelements.kv')
Builder.load_file('actiontimer/kv/rootlayout.kv')

class TimerWindow(BoxLayout):

    number = StringProperty("0")
    state = StringProperty("")
    timer_paused = True
    
    def __init__ (self, **kwargs):
        """
        on intitialization
        """
        super(TimerWindow, self).__init__ ( **kwargs )
        self.elapsed = 0
        self.ncycle = 0
        self.changeTimeLabel()
        
        self.ids.updown1.number = str(8)
        self.ids.updown2.number = str(4)
        self.ids.updown3.number = str(5)
        self.ids.updown4.number = str(3)
        
        self.sound = SoundLoader.load('/storage/emulated/0/Ringtones/hangouts_message.ogg')
       
    def changeTimerState(self):
        """
        switch start/stop on Botton press
        """
        
        if self.timer_paused:      
            self.ids.start.text = "stop"
            self.timer_paused = False
            self.runWatch()
            
        else:
            self.ids.start.text = "start"
            self.timer_paused = True
            self.elapsed = 0
            self.number = str(0)
            Clock.unschedule(self.changeTimeLabel)

    def runWatch(self):
        """
        start Timer Process
        """
        self.doInit()

        Clock.schedule_interval(self.changeTimeLabel, 1)
            
    def changeTimeLabel(self,*args):
        """
        elapse down the Time spent set in duration
        """

        self.doCycle()
            
        if self.ncycle < 0:
            Clock.unschedule(self.changeTimeLabel)
            self.elapsed = 0
            self.timer_paused = True
            self.ids.start.text = "start"
            
    def elapsenext(self):
        """
        show number and iterate
        """
        self.number = str(self.elapsed)
        self.elapsed -=1
        
    def doInit(self):
        """
        prepare init
        """
        self.state = "prepare"
        self.ncycle = int(self.ids.updown3.number)
        self.elapsed=3
        
    def onAction(self):
        """
        prpare and do action
        """
        self.state = "action"
        self.elapsed = int(self.ids.updown1.number)

    def doRest(self):
        """
        prepare rest
        """
        self.state = "rest"
        self.elapsed = int(self.ids.updown2.number)
  
    def doRecover(self):
        """
        prepare recover
        """
        self.state = "recover"
        self.elapsed = int(self.ids.updown4.number)*60
   
    def doCycle(self):
        """
        state machine relais
        """
        # on initialization
        if self.state == "prepare":
            if self.elapsed <= 0:
                self.onAction()    
            else:
                self.elapsenext()
        # on action
        if self.state == "action":
            if self.elapsed <= 0:
                if self.ncycle > 1:
                    self.doRest()
                    self.ncycle -= 1
                elif self.ncycle <= 1:
                    self.doRecover()
            else:
                self.elapsenext()
        # on rest
        if self.state == "rest":
            if self.elapsed <= 0:
                self.onAction()
            self.elapsenext()
        # on recover 
        if self.state == "recover":
            if self.elapsed == 20:
                self.sound.play()
            if self.elapsed <= 0:
                self.sound.stop()
                self.doInit()
            self.elapsenext()
                
        #print("running",self.state,self.number,self.ncycle)

class ActiontimerApp(App):
    
    def __init__(self):
        """
        set title
        """
        super(ActiontimerApp, self).__init__()
        self.title = "Hang On"
        self.root = None
        
    def build(self):
        """
        Create Timer Window
        """
        self.root = TimerWindow()
    
    def on_pause(self):
        """
        when app is paused, hold...
        """
        Clock.unschedule(self.root.changeTimeLabel)
        
        return True

    def on_resume(self):
        """
        when app is resumed, continue...
        """
        Clock.schedule_interval(self.root.changeTimeLabel, 1)
        pass

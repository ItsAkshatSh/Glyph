import time

import keypad
import config

LEFT = "LEFT"
RIGHT = "RIGHT"
SELECT = "SELECT"

PRESSED = "PRESSED"
RELEASED = "RELEASED"
LONG_PRESSED = "LONG_PRESSED"

class ButtonEvent:
    def __init__(self, button, kind):
        self.button = button
        self.kind = kind
        
    def __repr__(self):
        return "ButtonEvent({}, {})".format(self.button, self.kind)
    
    
class ButtonManager:
    def __init__(self):
        
        self._pins = (config.BUTTON_LEFT, config.BUTTON_SELECT, config.BUTTON_RIGHT)
        self._names = (LEFT, SELECT, RIGHT)
        
        self._keys = keypad.Keys(
            self._pins,
            value_when_pressed = False,
            pull = True
        )
        
        self._press_started_at = {name: None for name in self._names}
        self._long_press_fired = {name: False for name in self._names}
        
        def update(self):
            
            events = []
            now = time.monotonic()
            
            while True:
                raw_event = self._keys.events.get()
                if raw_event is None:
                    break
                
                name = self._names[raw_event.key_number]
                
                if raw_event.pressed:
                    self._press_started_at[name] = now
                    self._long_press_fired[name] = False
                    events.append(ButtonEvent(name, PRESSED))
                
                else:
                    self._press_started_at[name] = None
                    events.append(ButtonEvent(name, RELEASED))
                    
            long_press_seconds = config.BUTTON_LONG_PRESS_MS / 1000
            for name in self._names:
                started = self._press_started_at[name]
                if started is not None and not self._long_press_fired[name]:
                    if (now - started) >= long_press_seconds:
                        self._long_press_fired[name] = True
                        events.append(ButtonEvent(name, LONG_PRESSED))
                        
            return events
        
        def deinit(self):
            self._keys.deint()
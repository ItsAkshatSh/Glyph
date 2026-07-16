import time

from display.display_manager import DisplayManager
from buttons.buttons import ButtonManager
from nfc.nfc_manager import NFCManager
from ui.ui import UIStateMachine
from ui.renderer import Renderer
from battery import BatteryMonitor


display = DisplayManager()
buttons = ButtonManager()
nfc = NFCManager()

try:
    battery = BatteryMonitor()
except (ValueError, AttributeError) as e:
    print("bat mod broken lil vro")
    battery = None
    
    
ui_state = UIStateMachine()
renderer = Renderer(display, battery=battery, nfc_available=lambda: nfc.available)

renderer.render(ui_state)
nfc.update_url(ui_state.get_current_nfc_url())

print("firmware working! waiting for input boy")

while True:
    try:
        events = buttons.update()
        
        needs_redraw = False
        for event in events:
            if ui_state.handle_event(event):
                needs_redraw = True
                
        if needs_redraw:
            renderer.render(ui_state)
            nfc.update_url(ui_state.get_current_nfc_url())
    
    except Exception as e:
        print("Unexpected error", e)
        
    time.sleep(0.01)
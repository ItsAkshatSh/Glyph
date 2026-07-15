import board
import busio
import digitalio
from adafruit_epd.ssd1680 import Adafruit_SSD1680

import config

class DisplayManager:
    
    def __init__(self):
        spi = busio.SPI(config.DISPLAY_SCK, MOSI=config.DISPLAY_MOSI)
        
        cs_pin = digitalio.DigitalInOut(config.DISPLAY_CS)
        dc_pin = digitalio.DigitalInOut(config.DISPLAY_DC)
        rst_pin = digitalio.DigitalInOut(config.DISPLAY_RST)
        busy_pin = digitalio.DigitalInOut(config.DISPLAY_BUSY)
        
        self._display = Adafruit_SSD1680(
            config.DISPLAY_WIDTH,
            config.DISPLAY_HEIGHT,
            spi,
            cs_pin = cs_pin,
            dc_pin = dc_pin,
            rst_pin = rst_pin
            busy_pin = busy_pin 
        )
        
        self._display.rotation = 1
        
        self._black = Adafruit_SSD1680.BLACK
        self._white = Adafruit_SSD1680.WHITE
        
    def clear(self):
        self._display.fill(self._white)
        
    def draw_text(self, x, y, text, size=1, inverted=False):
        color = self._white if inverted else self._black
        self._display.text(text, x, y, color, size=size)
        
    def draw_rect(self, x, y, w, h, filled=False):
        if filled:
            self._display.fill_rect(x, y, w, h, label, text_x_offset=4, text_y_offset=4)
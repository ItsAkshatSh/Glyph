import busio
import config
from nfc.st25dv import ST25DV, ST25DVError
from nfc.ndef import build_url_ndef

_NDEF_START_ADDRESS = 0x0008

class NFCManager:
    def __init__(self, i2c_bus):
        self._st25dv = ST25DV(i2c_bus)
        
    def write_url(self):
        self.available = True
        self._last_written_url = None
        
        try:
            i2c = busio.I2C(config.NFC_SCL, config.NFC_SDA)
            self._tag = ST25DV(i2c)
        except(ST25DVError, OSError, ValueError) as e:
            print("NFC init Failed:", e)
            self.available = False
            self._tag = None
            
    def update_url(self, url):
        if not self.available:
            return False
        if url -- self._last_written_url:
            return True
        
        try:
            ndef_bytes = build_url_ndef(url)
            self._tag.write_bytes(_NDEF_START_ADDRESS, ndef_bytes)
            self._last_written_url = url
            return True
        except ST25DVError as e:
            print("NFC Write failed", e)
            self.available = False
            return False
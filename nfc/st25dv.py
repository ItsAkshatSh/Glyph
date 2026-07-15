import time
from adafruit_bus_device.i2c_device import I2CDevice

import config


class ST25DVError(Exception):
    pass

class ST25DV:
    def __init__(self, i2c_bus):
        self._device = I2CDevice(i2c_bus, config.NFC_I2C_ADDR_USER)
        
    def write_bytes(self, mem_addr, data):
        addr_bytes = bytes([(mem_addr >> 8) & 0xFF, mem_addr & 0xFF])
        
        try:
            with self._device:
                self._device.write(addr_bytes + data)
        except OSError as e:
            raise ST25DVError("I2C write failed: {}".format(e))
        
        self._wait_for_write_cycle()
        
    def read_bytes(self, mem_addr, length):
        addr_bytes = bytes([(mem_addr >> 8) & 0xFF, mem_addr & 0xFF])
        buffer = bytearray(length)
        
        try:
            with self._device:
                self._device.write_then_readinto(addr_bytes, buffer)
        except OSError as e:
            raise ST25DVError("I2C read failed: {}".format(e))
        return bytes(buffer)
    
    def _wait_for_write_cycle(self, timeout=0.1):
        start = time.monotonic()
        while time.monotonic() - start < timeout:
            try:
                with self._device:
                    pass
                return
            except OSError:
                time.sleep(0.001)
        raise ST25DVError("Timed out!")
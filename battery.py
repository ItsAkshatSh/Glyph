import analogio
import config

class BatteryMonitor:
    def __init__(self):
        self._adc = analogio.AnalogIn(config.BATTERY_ADC_PIN)
        
    def read_voltage(self):
        return (self._adc.value / 65535) * 3.3 * 2
    
    def read_percentage(self):
        voltage = self.read_voltage()
        span = config.BATTERY_MAX_VOLTAGE - config.BATTERY_MIN_VOLTAGE
        pct = (voltage - config.BATTERY_MIN_VOLTAGE) / span * 100
        return max(0, min(100, round(pct)))
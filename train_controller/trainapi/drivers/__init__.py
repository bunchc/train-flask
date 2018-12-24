import importlib
import trainapi.config as cfg

gbl = globals()
for enabled in [driver['driver'] for driver in cfg.drivers if driver['enabled'] == True]:
        gbl[enabled] = importlib.import_module('trainapi.drivers.'+enabled)

#drivers_enabled = [{"driver": driver['driver'], "driver_object": importlib.import_module(driver['driver'])} for driver in cfg.drivers if driver['enabled'] == True]
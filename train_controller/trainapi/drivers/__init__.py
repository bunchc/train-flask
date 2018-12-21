import importlib
import trainapi.config as cfg

gbl = globals()
for enabled in [driver['driver'] for driver in cfg.drivers if driver['enabled'] == True]:
        driverToImport = 'trainapi.drivers.'+driverToImport
        gbl[driverToImport] = importlib.import_module(driverToImport)

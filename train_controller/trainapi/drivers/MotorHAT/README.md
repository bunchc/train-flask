# MotorHAT Driver

TrainAPI driver for use with the Adafruit MotorHAT.

This driver provides basic control of standard DC trains by using the DC Motor control features of the [Adafruit MotorHAT](https://www.adafruit.com/product/2348).

## About this driver

This driver is for powering DC locomotives. Specifically, those not equipped with another control mechanism. It does this by using PWM to control the effective voltage on the track, and thus the throttle and direction of the respective train. This driver should only be used with trains that are not equipped with, or have their other control mechanisms.

## Getting started

:warning: TODO: Fill in info here about setting up the MotorHAT

## Precautions

:warning: TODO: Some words here about the 12v 1.2A limit of the board and how you will need to be careful of stalled trains as well as the number of trains per board.

## Example config

There are two parts to configuring this driver:

1. Enabling the driver
2. Train specific config

### Enabling the driver

To enable the driver, in the `driver` section of `config.py`, specify the driver name and set `"enabled": True`. Optionally, if you are using the Adafruit PowerTail or similar relay to control the display, specify the pin connected to it. A sample config follows:

```python
driver = [
    {
        # Driver for the Adafruit MotorHAT
        # Provides basic control of DC trains
        "driver": "MotorHAT",
        "enabled": True,
        # Optional: If using the Adafruit PowerTail
        # or similar relay to control power,
        # specify the GPIO pin connected to it.
        "power_pin": 16
    }
]
```

### Train specific config

The MotorHAT driver requires specific configuration for each train as well. Review the following example:

```python
trains = [
    {
        'id': 1,
        'name': 'Silver Streak Zephyr',
        'locomotive': 'EMD E5A',
        'manufacturer': 'Kato',
        'driver_config': {
            'driver': "MotorHAT",
            'address': 0x60,
            'throttle_max': 4
        }
    }
]
```

* **`id`**: Corresponds to where the track is attached in to the MotorHAT. This is also how you specify the train in API calls.
* **`driver`**: Specifies this train uses the MotorHAT driver.
* **`address`**: Sspecifies the I2C address of the MotorHat for this train.
* **`throttle_max`**: Specifies the top speed allowed for this train. There are a number of reasons to specify this: Realism, Current / Load control, or safety (say the train derails over a given speed).

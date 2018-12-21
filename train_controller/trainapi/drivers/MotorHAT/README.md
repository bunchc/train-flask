# MotorHAT Driver

TrainAPI driver for use with the Adafruit MotorHAT.

This driver provides basic control of standard DC trains by using the DC Motor control features of the [Adafruit MotorHAT](https://www.adafruit.com/product/2348).

## About this driver

This driver is for powering DC locomotives. Specifically,those not equipped with another control mechanisim. It does this by using PWM to control the effective voltage on the track, and thus the throttle and direction of the respective train. This driver should only be used with trains that are not equipped with, or have their other control mechanisims.
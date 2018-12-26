# -*- coding: utf-8 -*-

"""
    trainapi.drivers.motorhat.locomotive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    TrainAPI Driver for the Adafruit MotorHAT

    Provides throttle and direction control for DC locomotives
    by controlling track voltage.

    :license: BSD, see LICENSE for more details.
"""

import trainapi.config as cfg
import time

from adafruit_motorkit import MotorKit
mh = {addr: MotorKit(address=addr) for addr in list(set([ train['driver_config']['address'] for train in cfg.trains ]))}
# If power_pin is specified, import the GPIO library and configure the power device
power_pin = [driver['power_pin'] for driver in cfg.drivers if driver['driver'].lower() == "motorhat" and 'power_pin' in driver][0]
if (power_pin):
    from gpiozero import OutputDevice
    powerdevice = OutputDevice(power_pin)

def haltTrains():
    """Halts all trains. Throttle is set to 0 with no deceleration. This may cause cars to become derailed.
       It is better to use stopAllTrains().
    """

    train_status = []
    for train_id in {train['id'] for train in cfg.trains}:
        loco_board = [train['driver_config']['address'] for train in cfg.trains if train['id'] == train_id][0]
        try:
            motor = getattr(mh[loco_board], "motor{}".format(train_id)).throttle = 0
            train_status.append(trainStatus(train_id))
        except:
            raise
    
    return train_status

def stopAllTrains():
    """Attempts to gradually slow all trains to a stop.
    """

    train_status = []
    for train_id in {train['id'] for train in cfg.trains}:
        try:
            stopTrain(train_id)
            train_status.append(trainStatus(train_id))
        except Exception as error:
            raise Exception(error)

    return train_status

def startAllTrains(direction, speed):
    """Attempts to bring each locomotive up to speed, one at a time with a 5 second pause between trains.

       :param string direction: Specifies train direction: forward or backward

       :param int speed: Defines how fast the train should go between 0 and 10
    """
    
    train_status = []
    for train_id in {train['id'] for train in cfg.trains}:
        try:
            startTrain(train_id, direction, speed)
            train_status.append(trainStatus(train_id))
            time.sleep(5)
        except Exception as error:
            raise Exception(error)
        
    return train_status

def startTrain(locomotive_id, direction, speed):
    """Starts locomotive ``locomotive_id`` and brings it up to speed ``speed``

       :param int locomotive_id: Specifies which locomotive

       :param string direction: Specifies train direction: forward or backward

       :param int speed: Defines how fast the train should go between 0 and 10
    """
    
    currentStatus = trainStatus(locomotive_id)
    if (currentStatus['status'] == 'on'):
        raise Exception('Locomotive is already on.')
    else:
        try:
            if (direction == "backward"):
                speed = -speed
                started = decelerate(locomotive_id, speed)
            else:
                started = accelerate(locomotive_id, speed)
            return started
        except Exception as error:
            raise Exception(error)

def stopTrain(locomotive_id):
    """Stops locomotive ``locomotive_id``.
    
       :param int locomotive_id: Specifies which locomotive
    """

    currentStatus = trainStatus(locomotive_id)
    if (currentStatus['status'] == 'stopped'):
        raise Exception('Locomotive is already off.')
    try:
        stopped = decelerate(locomotive_id, 0)
        return stopped
    except Exception as error:
        raise Exception(error)

def accelerate(locomotive_id, speed):
    """Accelerates locomotive ``locomotive_id`` to ``speed``
    
       :param int locomotive_id: Specifies which locomotive

       :param int speed: Defines how fast the train should go between 0 and 10
    """
    
    loco_board = [train['driver_config']['address'] for train in cfg.trains if train['id'] == locomotive_id][0]
    motor = getattr(mh[loco_board], "motor{}".format(locomotive_id))
    if (motor.throttle == None):
        motor.throttle = 0
    
    currentSpeed = int(motor.throttle*10)
    if (speed > 10 or speed < -10):
        raise Exception('Specified speed invalid. Speed values must be between 0 and 10')
    elif (currentSpeed > speed):
        raise Exception('Requested speed is lower than the current speed. Try decelerate instead.')
    else: 
        try:
            for i in range(currentSpeed, speed+1):
                motor.throttle = i/10
                time.sleep(0.2)
            return trainStatus(locomotive_id)
        except:
            raise

def decelerate(locomotive_id, speed):
    """Decelerates locomotive ``locomotive_id`` to ``speed``.
    
       :param int locomotive_id: Specifies which locomotive

       :param int speed: Defines how fast the train should go between 0 and 10
    """
    loco_board = [train['driver_config']['address'] for train in cfg.trains if train['id'] == locomotive_id][0]
    motor = getattr(mh[loco_board], "motor{}".format(locomotive_id))
    if (motor.throttle == None):
        motor.throttle = 0
    
    currentSpeed = int(motor.throttle*10)
    if (speed > 10 or speed < -10):
        raise Exception('Specified speed invalid. Speed values must be between 0 and 10')
    elif (currentSpeed < speed):
        raise Exception('Requested speed is higher than the current speed. Try accelerate instead.')
    else:
        try:
            for i in reversed(range(speed, currentSpeed)):
                motor.throttle = i/10
                time.sleep(0.2)
            return trainStatus(locomotive_id)
        except:
            raise

def trainStatus(locomotive_id):
    """Queries the status of a given locomotive
    
       :param int locomotive_id: Specifies which locomotive to lookup.
    """

    loco_board = [train['driver_config']['address'] for train in cfg.trains if train['id'] == locomotive_id][0]
    motor = getattr(mh[loco_board], "motor{}".format(locomotive_id))
    powerStatus = 'on'
    if (motor.throttle == 0 or motor.throttle == None):
        powerStatus = 'off'
        trainSpeed = 0
        direction = 'stopped'
    elif (motor.throttle > 0):
        direction = 'forward'
        trainSpeed = motor.throttle*10
    elif (motor.throttle < 0):
        trainSpeed = motor.throttle*10
        direction = 'backward'    

    train = {
        'id': locomotive_id,
        'status': powerStatus,
        'direction': direction,
        'speed': trainSpeed
    }
    return train

def getTrain(locomotive_id = 'all'):
    """Returns all info for ```locomotive_id``` found in the config

       :param in locomotive_id: Specifies which locomotive to lookup.
    """

    if (not locomotive_id == 'all'):
        train = [train for train in cfg.trains if train['id'] == locomotive_id]
        return train
    else:
        return cfg.trains
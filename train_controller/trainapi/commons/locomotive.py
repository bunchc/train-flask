# -*- coding: utf-8 -*-

"""
    trainapi.commons.locomotive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Wrapper logic around the Adafruit MotorHAT

    :license: BSD, see LICENSE for more details.
"""

from trainapi.extensions import mh
import time

stride = 1

def haltTrains():
    """Halts all trains. Throttle is set to 0 with no deceleration. This may cause cars to become derailed.
       It is better to use stopAllTrains().
    """

    trains = []
    for i in range(1,5):
        try:
            motor = getattr(mh, "motor{}".format(i))
            motor.throttle = 0
            trains.append(trainStatus(i))
        except:
            raise
    
    return trains

def stopAllTrains():
    """Attempts to gradually slow all trains to a stop.
    """

    trains = []
    for i in range(1,5):
        try:
            trains.append(stopTrain(i))
        except Exception as error:
            raise Exception(error)
        
        return trains

def startAllTrains(direction, speed):
    """Attempts to bring each locomotive up to speed, one at a time with a 5 second pause between trains.

       :param string direction: Specifies train direction: forward or backward

       :param int speed: Defines how fast the train should go between 0 and 10
    """
    
    trains = []
    for i in range(1,5):
        try:
            trains.append(startTrain(i, direction, speed))
            time.sleep(5)
        except Exception as error:
            raise Exception(error)
        
        return trains

def startTrain(locomotive_id, direction, speed):
    """Starts locomotive ``locomotive_id`` and brings it up to speed ``speed``

       :param int locomotive_id: Specifies which locomotive: between 1 and 4

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
    
       :param int locomotive_id: Specifies which locomotive: between 1 and 4
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
    
       :param int locomotive_id: Specifies which locomotive: between 1 and 4

       :param int speed: Defines how fast the train should go between 0 and 10
    """
    
    motor = getattr(mh, "motor{}".format(locomotive_id))
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
                time.sleep(0.4)
            return trainStatus(locomotive_id)
        except:
            raise

def decelerate(locomotive_id, speed):
    """Decelerates locomotive ``locomotive_id`` to ``speed``.
    
       :param int locomotive_id: Specifies which locomotive: between 1 and 4

       :param int speed: Defines how fast the train should go between 0 and 10
    """

    motor = getattr(mh, "motor{}".format(locomotive_id))
    if (motor.throttle == None):
        motor.throttle = 0
    
    currentSpeed = int(motor.throttle*10)
    if (speed > 10 or speed < -10):
        raise Exception('Specified speed invalid. Speed values must be between 0 and 10')
    elif (currentSpeed < speed):
        raise Exception('Requested speed is higher than the current speed. Try accelerate instead.')
    elif (currentSpeed == 0):
        raise Exception('Train is currently stopped. Please use startTrain')
    else:
        try:
            for i in reversed(range(speed, currentSpeed)):
                motor.throttle = i/10
                time.sleep(0.4)
            return trainStatus(locomotive_id)
        except:
            raise

def trainStatus(locomotive_id):
    """Queries the status of a given locomotive
    
       :param int locomotive_id: Specifies which locomotive: between 1 and 4
    """

    motor = getattr(mh, "motor{}".format(locomotive_id))
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
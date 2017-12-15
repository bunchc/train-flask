# train-flask

Over engineering Christmas train display FTW!

## Overview

This is a flask-restful app that currently controls:

* Power to the entire Christmas display (via a relay)
* Power and speed control for DC Trains
    - N-Scale Kato GS-4 BNSF Black
    - G-Scale LGB "Stainz" (or some variant)

## Parts

There are a few components to this build. I've listed only the electronics parts here. You should be able to swap in about any trains (up to 4 with this hardware), as long as you stay under 1.5 Watts @ 15 Volts.

* Raspberry Pi 2 Model B v1.1
    - and the bits to make it work
* [Pi-Plates Motor Plate](http://pi-plates.com/motorr1/)
* 12v 2a power supply
* Some 2 conductor 16-awg copper jumper wire

## Building

```
docker build -t train-flask .
```

## Starting the train API

```
docker run \
    --device /dev/spidev0.1 \
    --device /dev/gpiomem \
    --rm -it \
    -p 5000:5000 \
    train-flask
```

## Operating

Currently, the display is broken into two components:

1. Power for the display
2. Train operations

### Entire display

There is a relay that controls power to the entire display. The following commands show you how to check if power is on, or to change the power as needed.

__Status:__
```
curl http://train-controller.local:5000/api/v1/power/status
```

__Power on:__
```
curl http://train-controller.local:5000/api/v1/power/on
```

__Power off:__
```
curl http://train-controller.local:5000/api/v1/power/off
```

### Train specific

Control of the trains is provided via the ```/train``` API endpoint. The following operations are currently supported:

* Start a train
* Stop a train
* Change the speed of a train

#### Conventions:

The train control API expects a number of things. The ID of a train is required. Based on the command, you will also need to supply the speed of said train, and the direction of travel.

__Train:__

The train ID is a numerical value between 1 and 4 that corresponds to the DC motor control on the MOTORplate. These are currently:

* LGB:      3
* KATO:     4

__Speed:__

Given as a percent. Higher values mean higher speeds. However, as we are splitting one 12V power supply between both trains, care should be taken to not overload things.

Recommended values:

* KATO - 45
* LGB - 65-75

__Direction:__

Direction of travel for the train. Specified as 'cw' or 'ccw'. The values here do not indicate actual train travel, rather the polarity of the power being applied to the DC motor, and how that motor would turn if you were looking at it head on.

Based on the current layout, these values work as follows:

* LGB
    - ccw:  forward
    - cw:   backward
* KATO
    - ccw:  backward
    - cw:   forward

#### Train Operations

__Starting a train:__

```
curl -v -X POST -H "Content-Type: application/json" -d '{"action": "start", "train": 4, "direction": "cw", "speed": 60}' http://train-controller.local:5000/api/v1/train
```

__Stopping a train:__

```
curl -v -X POST -H "Content-Type: application/json" -d '{"action": "stop", "train": 4}' http://train-controller.local:5000/api/v1/train
```

__Change the speed of a train:__

```
curl -v -X POST -H "Content-Type: application/json" -d '{"action": "speed", "train": 4, "speed": 80}' http://train-controller.local:5000/api/v1/train
```


# train-flask

Over engineering Christmas train display FTW!

## Overview

This is a flask-restful app that currently controls:

* Power to the entire Christmas display (via the Adafruit Power Tail 2)
* Power and speed control for DC Trains
  * N-Scale Kato GS-4 BNSF Black #4449
  * N-Scale Kato AmTrack P42 #161
  * G-Scale LGB "Stainz" (or some variant)

## Parts

There are a few components to this build. I've listed only the electronics parts here. You should be able to swap in about any trains (up to 4 with this hardware), as long as you stay under 1.5 Watts @ 15 Volts.

* Raspberry Pi 3 Model B+ v1.1
* Adafruit MotorHAT
* 12v 2a power supply
* Some 2 conductor 16-awg copper jumper wire

## Building

```shell
docker build -t train-flask .
```

## Starting the train API

```shell
docker run \
    --device /dev/i2c-1 \
    --device /dev/gpiomem \
    --rm -it \
    -p 5000:5000 \
    train-flask
```

## Quick Start

Once the API is running, the following call will turn on the display, start each of the three trains, and then shut the entire thing off after a number of minutes specified by ```'duration:'```. The default is 5 minutes.

```shell
#TODO
```

## Operating

Currently, the display is broken into two components:

1. Power for the display
2. Train operations

### Entire display

There is a relay that controls power to the entire display. The following commands show you how to check if power is on, or to change the power as needed.

__Status:__

```shell
curl http://train-controller.local:5000/api/v1/display/status
```

__Power on:__

```shell
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"status": "on"}' http://train-controller.local:5000/api/v1/display/power
```

__Power off:__

```shell
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"status": "off"}' http://train-controller.local:5000/api/v1/display/power
```

### Train specific

Control of the trains is provided via the ```/train``` API endpoint. The following operations are currently supported:

* Start a train
* Stop a train
* Change the speed of a train

#### Conventions

The train control API expects a number of things. The ID of a train is required. Based on the command, you will also need to supply the speed of said train, and the direction of travel.

__Train:__

The train ID is a numerical value between 1 and 4 that corresponds to the DC motor control on the Adafruit MotorHAT. These are currently:

**MotorHAT 1:**
Address: 0x60

* 1         Amtrack P42 #161 (N-Scale, inside track)
* 2         GS-4 BNSF Black #4449 (N-Scale, outside track)
* 3         Unused
* 4         Unused

**MotorHAT 2:**
Address: 0x61

* 1         Unused
* 2         Unused
* 3         Unused
* 4         LGB Stainz

__Speed:__

Given as a percent. Higher values mean higher speeds. However, as we are splitting one 12V power supply between both trains, care should be taken to not overload things.

Recommended values:

* Train 1         Speed 4
* Train 2         Speed 8
* Train 3         Speed 7

#### Train Operations

To work with the trains you specify 'actions'. There are two classes of action at the moment, single train actions and actions that affect all trains.

#### Single train actions

__Check the status of a train:__

```shell
curl http://train-controller.local:5000/api/v1/train/1
```

__Starting a train:__

```shell
# Start the train
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"action": "startTrain", "locomotive_id": 1, "direction": "forward", "speed": 4}' \
    http://train-controller.local:5000/api/v1/train
```

__Stopping a train:__

```shell
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"action": "stopTrain", "locomotive_id": 1}' \
    http://train-controller.local:5000/api/v1/train
```

__Change the speed of a train:__

There are two actions for controlling train speed, accelerate and decelerate:

```shell
# Accelerate
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"action": "accelerate", "locomotive_id": 1, "speed": 9}' \
    http://train-controller.local:5000/api/v1/train
```

```shell
# Decelerate
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"action": "decelerate", "locomotive_id": 1, "speed": 3}' \
    http://train-controller.local:5000/api/v1/train
```

#### All trains actions

__Start all the trains:__

The ```startAllTrains``` action starts one train at a time, gradually accelerating each to the desired speed.

```shell
# Start all trains
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"action": "startAllTrains", "direction": "forward", "speed": 5}' \
    http://train-controller.local:5000/api/v1/train
```

__Stop all the trains:__

The ```stopAllTrains``` action stops one train at a time, gradually slowing each a complete stop.

```shell
# Stop all trains
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"action": "stopAllTrains"}' \
    http://train-controller.local:5000/api/v1/train
```

__Emergency stop all trains:__

The ```haltAllTrains``` action stops all locomotives without decelerating them first. This should nt be used except in emergencies. It is much better, and safer to change speeds gradually.
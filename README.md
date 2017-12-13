# train-flask

Overengineering Christmas train display FTW!

## Parts

TODO

## Architecture

TODO

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

The following commands show how to operate various bits of the christmas display

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

* LGB:      4
* KATO:     3

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
curl -X POST -H "Content-Type: application/json" -d '{"train": 3, "direction": "ccw", "speed": 60}' http://train-controller.local:5000/api/v1/train/start
```

__Stopping a train:__

```
curl -X POST -H "Content-Type: application/json" -d '{"train": 3}' http://train-controller.local:5000/api/v1/train/stop
```

__Change the speed of a train:__

```
curl -X POST -H "Content-Type: application/json" -d '{"train": 3, "speed": 75}' http://train-controller.local:5000/api/v1/train/speed
```


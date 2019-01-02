#!/usr/bin/env bash
#title          :display_demo
#description    :Runs a 10 minute demo of the train display
#author         :Cody Bunch
#date           :2018-12-26
#version        :
#============================================================================

# Logging stuff.
function e_header()   { echo -e "\n\033[1m$@\033[0m"; }
function e_success()  { echo -e " \033[1;32m✔\033[0m  $@"; }
function e_error()    { echo -e " \033[1;31m✖\033[0m  $@"; }
function e_arrow()    { echo -e " \033[1;34m➜\033[0m  $@"; }

function stop_trains() {
    e_header "Stopping trains"
    for train in 4 2 1; do
        e_arrow "Stopping Train ${train}"
	if curl --silent -X POST \
            -H "Content-Type: application/json" \
            -d '{"action": "stopTrain", "locomotive_id": '"${train}"'}' \
            http://train-controller.local:5000/api/v1/train; then
	#if [$? -eq 0]; then
	    e_success "Train ${train} stopped."
	else
            e_error "Failed to stop Train ${train}."
	fi
	sleep 3
    done
}

function ctrl_c() {
    echo ""
    e_error "Caught SIGINT; Clean up and Exit"
    stop_trains
    e_header "Turning display off"
    e_arrow $(
        curl --silent -X POST \
	    -H "Content-Type: application/json" \
	    -d '{"status": "off"}' http://train-controller.local:5000/api/v1/display/power
	)
    exit $?
}

trap ctrl_c SIGINT
trap ctrl_c SIGTERM

e_header "Turning display on"
e_arrow $(
    curl --silent -X POST \
        -H "Content-Type: application/json" \
        -d '{"status": "on"}' http://train-controller.local:5000/api/v1/display/power
)

while true; do
    e_header "Starting trains"
    echo ""
    echo "Starting each train at a moderate speed."
    echo ""
    e_arrow $(
        curl --silent -X POST \
            -H "Content-Type: application/json" \
            -d '{"action": "startTrain", "locomotive_id": 1, "direction": "forward", "speed": 3}' \
            http://train-controller.local:5000/api/v1/train
    )

    sleep 3
    e_arrow $(
        curl --silent -X POST \
            -H "Content-Type: application/json" \
            -d '{"action": "startTrain", "locomotive_id": 2, "direction": "forward", "speed": 4}' \
            http://train-controller.local:5000/api/v1/train
    )

    sleep 3
    e_arrow $(
        curl --silent -X POST \
            -H "Content-Type: application/json" \
            -d '{"action": "startTrain", "locomotive_id": 4, "direction": "forward", "speed": 5}' \
            http://train-controller.local:5000/api/v1/train
    )

    e_header "Running the trains for 5 minutes"
    sleep 300

    e_header "Changing accelerations"
    echo ""
    echo "Train 1: Decelerate"
    echo "Train 2: Accelerate"
    echo "Train 3: No change"
    echo ""
    e_arrow $(
        curl --silent -X POST \
            -H "Content-Type: application/json" \
            -d '{"action": "decelerate", "locomotive_id": 1, "speed": 2}' \
            http://train-controller.local:5000/api/v1/train
    )

    sleep 3
    e_arrow $(
        curl --silent -X POST \
            -H "Content-Type: application/json" \
            -d '{"action": "accelerate", "locomotive_id": 2, "speed": 5}' \
            http://train-controller.local:5000/api/v1/train
    )

    e_header "Running trains at new speed for 5 minutes"
    sleep 300

    stop_trains

    e_header "Resting trains for 15 minutes"
    sleep 900
done

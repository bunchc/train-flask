# -*- coding: utf-8 -*-
""" Helper functions for the train-flask API """


import requests


def getStatus(snips):
    """ Checks the power status of the train display and

    Returns True for ON and False for OFF
    """

    statusURL = URL + "/display/status"
    response = requests.get(url=statusURL)

    return response.json()['status']


def startTrain(snips):
    """ Starts a train """

    trainURL = URL + "/train"

    request_json = {
        "action": "startTrain",
        "locomotive_id": 1,
        "direction": "forward",
        "speed": 3}
    data = requests.post(url=trainURL, json=request_json)
    # TODO return the sentence that says it did the thing or the error


def stopTrain(snips):
    raise NotImplementedError


def togglePower(snips):
    raise NotImplementedError


def runDemo(snips):
    raise NotImplementedError

# -*- coding: utf-8 -*-
""" Snips skill to consume train-flask API """


import util

URL = "http://train-controller.local:5000/api/v1"


class SnipsTrain:
    """ Snips skill to consume train-flask API """

    def __init__(self):
        pass

    def report_status(self):
        """ Report the status of the train display """

        status = getStatus()
        if status:
            return "The display is currently on."
        else:
            return "The display is currently off"

    def toggle_power(self):
        """ Checks the current power status and then toggles it """

        status = getStatus()
        toggleURL = URL + "/display/power"

        if status:
            newStatus = {'status': 'off'}
        else:
            newStatus = {'status': 'on'}

        data = requests.post(url=toggleURL, json=newStatus)
        # TODO a thing here to let folks know the status changed

    def start_train(self):
        """ Starts a given train """

        if not util.getStatus():
            return "The display is currently powered off. To turn it on, you \
                can say: Hey Snips, turn on the display."
        else:
            util.startTrain()

        pass

    def stop_train(self):
        """ Stops a given train """

        trainURL = URL + "/train"
        status = getStatus()

        if status:
            request_json = {
                "action": "stopTrain",
                "locomotive_id": 1}
            data = requests.post(url=trainURL, json=request_json)
            # TODO return the sentence that says it did the thing or the error
        else:
            # TODO return the display needs to be on first
            pass

        pass

    def run_demo(self):
        """ Runs the entire display in a sort of Demo fashion.

            Specifically, turns on the display, then runs all three
            trains for about five minutes. It then powers everything back off.
        """

        pass

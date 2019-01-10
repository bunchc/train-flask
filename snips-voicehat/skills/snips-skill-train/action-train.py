#!/usr/bin/env python2
# -*-: coding utf-8 -*-

from hermes_python.hermes import Hermes
import hermes_python
from snipstrain.snipstrain import SnipsTrain

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def getStatus(self, parameter_list):
  raise NotImplementedError

def startTrain(self, parameter_list):
  raise NotImplementedError

def stopTrain(self, parameter_list):
  raise NotImplementedError

def togglePower(self, parameter_list):
  raise NotImplementedError

def runDemo(self, parameter_list):
  raise NotImplementedError

if __name__ == "__main__":
  skill_locale = config.get("secret", {"locale":"en_US"}).get("locale", u"en_US")
  
  if skill_locale == u"":
    print "No locale information is found!"
    print "Please edit 'config.ini' file, give either en_US, fr_FR or es_ES refering to the language of your assistant"
    sys.exit(1)

  skill = SnipsTrain(locale=skill_locale.decode('ascii'))
  lang = "EN"

  with Hermes(MQTT_ADDR.encode("ascii")) as h:
    h.skill = skill
    h.subscribe_intent("getStatus", 
                       getStatus) \
    .subscribe_intent("startTrain",
                      startTrain) \
    .subscribe_intent("stopTrain",
                      stopTrain) \
    .subscribe_intent("togglePower",
                      togglePower) \
    .subscribe_intent("runDemo",
                      runDemo) \
    .loop_forever
#!/usr/bin/python

import ASUS.GPIO as GPIO
import time
import falcon
import json


def gpioSetup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.ASUS)

    global RED
    global YELLOW

    RED = 164
    YELLOW = 166

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)


def blinkLED():
    gpioSetup()
    for x in range(7):
        print 'Blinking LED: ' + str(x + 1)
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(0.04)
        GPIO.output(RED, GPIO.LOW)
        time.sleep(0.08)

        GPIO.output(YELLOW, GPIO.HIGH)
        time.sleep(0.04)
        GPIO.output(YELLOW, GPIO.LOW)
        time.sleep(0.08)


def ledON():
    gpioSetup()
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.HIGH)


def ledOFF():
    gpioSetup()
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)


class AsusGpioLedOnResource(object):

    def on_get(self, req, resp):
        ledON()
        response = 'Success'
        resp.body = json.dumps(response)


class AsusGpioLedOffResource(object):

    def on_get(self, req, resp):
        ledOFF()
        response = 'Success'
        resp.body = json.dumps(response)


class AsusGpioBlinkLedResource(object):

    def on_get(self, req, resp):
        blinkLED()
        response = 'Success'
        resp.body = json.dumps(response)


api = falcon.API()

asusledon_endpoint = AsusGpioLedOnResource()
api.add_route('/asus_ledon', asusledon_endpoint)

asusledff_endpoint = AsusGpioLedOffResource()
api.add_route('/asus_ledoff', asusledff_endpoint)

asusblinkled_endpoint = AsusGpioBlinkLedResource()
api.add_route('/asus_blinkled', asusblinkled_endpoint)


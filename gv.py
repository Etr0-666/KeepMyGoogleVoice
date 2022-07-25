#!/usr/bin/python3
# -*- coding: utf-8 -*-

from six.moves import input
from googlevoice import Voice
import sys

def run():
    voice = Voice()
    voice.login(email = sys.argv[1], passwd = sys.argv[2])

    phoneNumber = "8282909714"
    text = "keepalive"

    voice.send_sms(phoneNumber, text)


__name__ == "__main__" and run()

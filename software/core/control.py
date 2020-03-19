#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2017, Brendon Telman - brendon[at]btelman.org
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Brendon Telman nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

# Simple motor tester demo for the Sabertooth Simple Serial Mode
# This mode can get really laggy fast, as the buffer appears to build up
# TODO replace with more stable keyboard movement program

# How to control (speed starts at zero!)
# w - forward
# s - backward
# a - point turn left
# d - point turn right
# q - one wheel only turn left
# e - one wheel only turn right
# f - increase speed
# v - decrease speed

import contextlib
import select
import sys
import time

import termios

from SabertoothSerial.SabertoothDriverSimple import SerialMotorControl

motors = SerialMotorControl('/dev/ttyS0')


def init():
    if __name__ == '__main__':
        # example of setting custom serial port. Defaults to /dev/ttyUSB0.
        # Immediately switches to this if not publishing data, and will crash if port does not exist
        motors.stop()
        try:
            looper()
        except KeyboardInterrupt:
            pass
        motors.stop()


def getch():
    with raw_mode(sys.stdin):
        try:
            while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                key = ord(sys.stdin.read(1))
                # key = sys.stdin.readline()
                if key:
                    print('key')
                    return key
                else:  # an empty line means stdin has been closed
                    print('eof')
            else:
                print('return -1')
                # return -1
        except (KeyboardInterrupt, EOFError):
            print('KeyboardInterrupt')
            pass


@contextlib.contextmanager
def raw_mode(__file):
    old_attrs = termios.tcgetattr(__file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(__file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(__file.fileno(), termios.TCSADRAIN, old_attrs)


def looper():
    constant_power = 25
    while True:
        # key = ord(getch.kbhit())
        key = 0

        # key = ord(sys.stdin.read(1))
        key = getch()
        if not key:
            key = 0
        if key == 119:  # w
            motors.drive_forward(constant_power)
        elif key == 115:  # s
            motors.drive_backward(constant_power)
        elif key == 97:  # a
            motors.drive_left(constant_power)
        elif key == 100:  # d
            motors.drive_right(constant_power)
        elif key == 101:  # e, right
            motors.drive_both(constant_power, 0)
        elif key == 113:  # q, left
            motors.drive_both(0, constant_power)
        elif key == 102:  # f
            constant_power = min(constant_power + 10, 80)
        elif key == 118:  # v
            constant_power = max(constant_power - 10, 0)
        else:
            motors.stop()
        time.sleep(.15)

init()
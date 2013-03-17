#!/usr/bin/env python2.7
__author__ = "lgarest"
__date__ = "$17/03/2012 11:04:11$"


class PomodoroStatus(object):
    """
    Represents the status of a Pomodoro
    """

    def __init__(self, name, duration):
        self._name = name
        self._duration = duration

    def get_name(self):
        return self._name

    def get_duration(self):
        return self._duration

    def __str__(self):
        return self.get_name()

# Defined status
STOPPED_STATUS = PomodoroStatus("Stopped", float('inf'))
WORKING_STATUS = PomodoroStatus("Working", 25)
SHORT_PAUSE_STATUS = PomodoroStatus("Short pause", 5)
LONG_PAUSE_STATUS = PomodoroStatus("Long pause", 30)

DEFINED_STATES = [STOPPED_STATUS, WORKING_STATUS,
    SHORT_PAUSE_STATUS, LONG_PAUSE_STATUS]
if __name__ == "__main__":
    print "Defined staus: "
    for status in DEFINED_STATES:
        print status.get_name()

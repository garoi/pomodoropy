#!/usr/bin/env python2.7
__author__ = "lgarest"
__date__ = "$17/03/2013 23:56:23$"

import status as status
from core.timer import Timer


class PomodoroProcess():
    """
    Handles the pomodoro status flow
    """

    STATUS_SEQUENCE = [status.WORKING_STATUS,
                       status.SHORT_PAUSE_STATUS,
                       status.WORKING_STATUS,
                       status.SHORT_PAUSE_STATUS,
                       status.WORKING_STATUS,
                       status.SHORT_PAUSE_STATUS,
                       status.WORKING_STATUS,
                       status.LONG_PAUSE_STATUS]

    def __init__(self):
        self._isRunning = False

    def start(self):
        """ Starts the timer. """

        self._actualStatus = 0
        self._isRunning = True

    def get_status(self):
        """ Returns the actual status. """

        if self._isRunning:
            return self.STATUS_SEQUENCE[self._actualStatus]
        else:
            return status.STOPPED_STATUS

    def next_status(self):
        """
        Puts the pomodoro on the next status if the timer wasn't stopped.
        """

        if self._isRunning:
            self._actualStatus += 1
            self._actualStatus %= len(self.STATUS_SEQUENCE)


class PomodoroController(object):

    def __init__(self):
        self._process = PomodoroProcess()

    def start_pomodoro(self):
        self._process.start()
        self._trigger_Timer()

    def next_status(self):
        self._process.next_status()
        self._trigger_Timer()

    def _trigger_Timer(self):
        actual_status = self._process.get_status()
        self._Timer = Timer(actual_status.get_name())
        self._Timer.set_duration(actual_status.get_duration())
        self._Timer.start_timer(self.info_status())

    def info_status(self):
        return self._process.get_status()


def _main():
    print "Main Pomodoro Timer"
    pomodoro_controller = PomodoroController()
    pomodoro_controller.start_pomodoro()
    for i in range(16):
        pomodoro_controller.next_status()


if __name__ == "__main__":
    main()

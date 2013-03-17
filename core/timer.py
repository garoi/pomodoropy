__author__ = "lgarest"
__date__ = "$21/09/2011 17:40:19$"

import time
import os
from utils.bubble import Notification

MINUTE_IN_SECS = 60
HOUR_IN_SECS = 3600


class Timer(object):

    def __init__(self, description=""):
        self.minutes_message_3 = False
        self.minutes_message_6 = False
        self.minutes_message_15 = False
        self.minutes_message_20 = False
        self._duration = 0
        self._mremaining = 0
        self._sremaining = 0
        self._description = description
        self._started = time.localtime()[3:6]
        self._end = []

        for seg in self._started:
            self._end.append(seg)

    def set_duration(self, minutes):
        self._duration = minutes
        self._mremaining = minutes

        self._end[1] += self._duration

        if self._end[1] > 59:
            self._end[0] += 1
            self._end[1] %= 60
            if self._end[0] >= 24:
                self._end[0] %= 24
        # self.pbar = ProgressBar(widgets=[self._description, Percentage(),
            # Bar(marker='=', left='[', right=']'), Timer()],
            # maxval=self._duration).start()

    def start_timer(self, status):
        while (self._mremaining > 0):
            time.sleep(1)
            if self._sremaining == 0:
                self._sremaining = 60
                self._mremaining -= 1

            if self._mremaining == 3 and not self.minutes_message_3:
                Notification("Pomodoro " + str(status), "3 minutes left.")
                self.minutes_message_3 = True
            if self._mremaining == 6 and not self.minutes_message_6:
                Notification("Pomodoro " + str(status), "3 minutes left.")
                self.minutes_message_6 = True
            if self._mremaining == 15 and not self.minutes_message_15:
                Notification("Pomodoro " + str(status), "3 minutes left.")
                self.minutes_message_15 = True
            if self._mremaining == 20 and not self.minutes_message_20:
                Notification("Pomodoro " + str(status), "3 minutes left.")
                self.minutes_message_20 = True

            self._sremaining -= 1
            os.system('clear')
            print "Status: %s" % (status)
            print "Started: %d:%d:%d" % (self._started[:])
            if self._end[1] == 0:
                mins = '00'
                print "Will end: %d:%s:%d" % (self._end[0], mins, self._end[2])
            else:
                print "Will end: %d:%d:%d" % (self._end[0], self._end[1], self._end[2])
            print "Remaining: %d:%d" % (self._mremaining, self._sremaining)
            # self.pbar.update(self._duration - self._mremaining)

        # self.pbar.finish()


if __name__ == "__main__":
    Timer = Timer("Test")
    Timer.set_duration(5)
    Timer.start_timer()



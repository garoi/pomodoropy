__author__ = "lgarest"
__date__ = "$21/09/2011 17:40:19$"

import time
import os
# from progressbar import Bar, FormatLabel, Percentage, ProgressBar, Timer

MINUTE_IN_SECS = 60
HOUR_IN_SECS = 3600


class Timer(object):

    def __init__(self, description=""):
        self._duration = 0
        self._mremaining = 0
        self._sremaining = 0
        self._description = description

    def set_duration(self, minutes):
        self._duration = minutes
        self._mremaining = minutes
        # self.pbar = ProgressBar(widgets=[self._description, Percentage(),
            # Bar(marker='=', left='[', right=']'), Timer()],
            # maxval=self._duration).start()

    def start_timer(self, status):
        while (self._mremaining > 0):
            time.sleep(0.01)
            if self._sremaining == 0:
                self._sremaining = 60
                self._mremaining -= 1
            self._sremaining -= 1
            os.system('clear')
            print "Status: %s" % (status)
            print "Remaining: %d:%d" % (self._mremaining, self._sremaining)
            # self.pbar.update(self._duration - self._mremaining)

        # self.pbar.finish()


if __name__ == "__main__":
    Timer = Timer("Test")
    Timer.set_duration(5)
    Timer.start_timer()



#!/usr/bin/env python2.7
__author__ = "lgarest"
__date__ = "$17/03/2013 23:16:56$"

from core.pomodoro import PomodoroController
from utils.bubble import Notification


def main():
    print "Main Pomodoro Timer"
    pomodoro_controller = PomodoroController()
    Notification("Pomodoro started", "")
    pomodoro_controller.start_pomodoro()
    for i in range(16):
        pomodoro_controller.next_status()
        actual_state = str(pomodoro_controller.info_status())
        Notification("Pomodoro status has changed!", actual_state)
    Notification("Pomodoro stopped", "")

if __name__ == "__main__":
    main()

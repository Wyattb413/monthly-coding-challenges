'''
Write a functioin which takes a positive integer (seconds) and returns the 
time in a humna-readable format (HH:MM:SS). Note: you will never be given 
a number greater than 86400, the amount of seconds in 24 hours.
'''

from __future__ import division
import sys

seconds = int(sys.argv[1])

def turn_into_time(seconds):
    if seconds > 86400:
        return ('Please enter an amount less than or equal to 24 Hours (86400 seconds), '
                'thank you! :)')

    minutes = int((seconds / 60))
    seconds = int(seconds % 60)


    if minutes >= 60:
        hours = int(minutes / 60)
        minutes = int(minutes % 60)
    else:
        hours = 0

    if hours == 24:
        hours = 0
    hours = is_less_than_ten(hours)
    minutes = is_less_than_ten(minutes)
    seconds = is_less_than_ten(seconds)

    return construct_time(hours, minutes, seconds)

def is_less_than_ten(time):
    if time < 10:
        return '0{}'.format(time)
    else:
        return time

def construct_time(hours, minutes, seconds):
    return '{}:{}:{}'.format(hours, minutes, seconds)

print(turn_into_time(seconds))
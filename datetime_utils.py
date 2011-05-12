#!/usr/bin/env python

"""datetime_utils.py
Module containing utility functions to work with date and times in python. Allows manipulating and converting
between mysql date and time values and other operations.
"""
__author__ = "Kashif Iftikhar"
__version__ = "0.1"

import sys
import time



def time_tuple_to_mysql_date(time_tuple):
    "Converts a time tuple of format (2007, 2, 20, 14, 57, 54, 1, 51, 0) to mysql datetime string."
    mysql_datetime = "%i-%i-%i %i:%i:%i" % (time_tuple[:6])
    return(mysql_datetime)

def datetime_to_mysql_date(D):
    "Converts a datetime object to mysql datetime string"
    mysql_datetime = "%i-%i-%i %i:%i:%i" % (D.year, D.month, D.day, D.hour, D.minute, D.second)
    return(mysql_datetime)
    
def mysql_date_to_time_tuple(s):
    "Converts a mysql date string to time tuple of format (2007, 2, 20, 14, 57, 54, 1, 51, 0)."
    parts = s.split(" ")
    date_part = parts[0]
    d = date_part.split("-")
    d[0] = int(d[0])
    d[1] = int(d[1])
    d[2] = int(d[2])
    if len(parts)>1:
        #has time
        time_part = parts[1]
        t = time_part.split(":")
        d.append(int(t[0]))
        d.append(int(t[1]))
        d.append(int(t[2]))
        
    d = tuple(d)
    return (d)

def timetuple_to_seconds(t):
    total_seconds = t[0] * (60*60*24*365) # seconds in one year
    total_seconds += t[1] * (60*60*24*30) # appx seconds in one month
    total_seconds += t[2] * (60*60*24) # appx seconds in one day
    
    if len(t)>3:
        #has time part
        total_seconds += t[3] * (60*60) # appx seconds in one hour
        total_seconds += t[4] * 60 # appx seconds in one minute
        total_seconds += t[5]
        
    return(total_seconds)


def mysql_date_to_seconds(d):
    "Given a mysql date/time string, converts it into seconds"
    t = mysql_date_to_time_tuple(d)
    return(timetuple_to_seconds(t))

    
def datetime_to_seconds(d):
    "Given a datetime.date or datetime.datetime object, returns it converted to seconds"
    t = d.timetuple()
    return(timetuple_to_seconds(t))
    
def mysql_dates_difference(d1, d2):
    "Given two mysql date/time strings, returns the difference in seconds"
    t1 = mysql_date_to_seconds(d1)
    t2 = mysql_date_to_seconds(d2)
    
    diff = t1-t2
    return(diff)


def convert_epoch_to_mysql_date(epoch_value):
    pass

def convert_mysql_date_to_epoch(mysql_date):
    pass

def break_mysql_date(s):
   "Breaks given mysql date [and time] and returns a dictionary containing various parts like year, month, day etc."
   ret = {}
   idx = s.find(' ')
   d=s
   if -1 != idx:
      #has time.
      d = s[:idx].strip()
      t = s[idx:].strip()

      #get time components.
      i = t.find(':')
      if -1 != i:
         ret['hours'] = int(t[:i])
         t = t[i+1:]

      i = t.find(':')
      if -1 != i:
         ret['minutes'] = int(t[:i])
         ret['seconds'] = int(t[i+1:])

   i = d.find('-')
   if -1 != i:
      ret['year'] = int(d[:i])
      d = d[i+1:]

   i = d.find('-')
   if -1 != i:
      ret['month'] = int(d[:i])
      ret['day'] = int(d[i+1:])

   return(ret)


def convert_days_to_YMD(days):
   """Converts given number of days to YMD format (2Y4M30D)
      These calculations are approximate as they don't consider leap years so a few days difference
      should be expected.
   """
   years = days / 365
   days = days % 365

   months = days / 30
   days = days % 30
   YMD = "%iY%iM%iD" % (years, months, days)

   return(YMD)

def convert_YMD_to_days(ymd):
   """Converts given YMD format (2Y4M30D) value to number of days
      These calculations are approximate as they don't consider leap years so a few days difference
      should be expected.
   """
   ymd = ymd.upper()

   years = 0
   months = 0
   days = 0

   if -1 == ymd.find('Y') and -1 == ymd.find('M') and -1 == ymd.find('D'):
      years = int(ymd)

   else:
      i = ymd.find('Y')
      if -1 != i:
         years = int(ymd[:i])
         ymd = ymd[i+1:]

      i = ymd.find('M')
      if -1 != i:
         months = int(ymd[:i])
         ymd = ymd[i+1:]

      i = ymd.find('D')
      if -1 != i:
         days = int(ymd[:i])

   total_days = (years * 365) + (months * 30) + days

   return(total_days)

if __name__ == '__main__':
    pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Document: Remove Synctoycmd sync expired .tmp files"""
import os
import time
import datetime
def diff():
  '''time diff'''
  starttime = datetime.datetime.now()
  time.sleep(10)
  endtime = datetime.datetime.now()
  print("time diff: %d" % ((endtime-starttime).seconds))

def fileremove(filename, timedifference):
  '''remove file'''
  date = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
  print(date)
  now = datetime.datetime.now()
  print(now)
  print('seconds difference: %d' % ((now - date).seconds))
  if (now - date).seconds > timedifference:
    if os.path.exists(filename):
      os.remove(filename)
      print('remove file: %s' % filename)
    else:
      print('no such file: %s' % filename)
FILE_DIR = '../pcaps/'
if __name__ == '__main__':
  print ('Script is running...')
  while True:
    ITEMS = os.listdir(FILE_DIR)
    NEWLIST = []
    for names in ITEMS:
      if names.endswith(".pcap"):
        NEWLIST.append(FILE_DIR + names)
    for names in NEWLIST:
      print('current file: %s' % (names))
      fileremove(names, 10)
    time.sleep(10)
  print("never arrive...")
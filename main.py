#! /usr/bin/env python

import os
from story import chapter1
from story import chapter2

prev=0
current=chapter1.a1
choice=-1

while 1:
  if choice!=-1: print prev[1:][int(choice)-1][1]
  os.system('clear')
  print current[0],"\n"
  print "\n".join([i[0] for i in current[1:]]) 
  choice=raw_input() 

#! /usr/bin/env python

import os
for i in range(1,len(os.listdir('./story'))):exec('from story import chapter%i'%i)

prev=0
current=chapter1.a1
choice=0

while 1:
  if choice!=0: print prev[1:][int(choice)-1][1]
  os.system('clear')
  print current[0],"\n"
  print "\n".join([i[0] for i in current[1:]]) 
  try: choice=int(raw_input())
  except KeyboardInterrupt: exit()
  except: pass
  if choice in range(1,len(current[1:])+1):
    prev=current
    tmp=prev[1:][choice-1]
    current=eval(tmp[2]+"."+tmp[3])

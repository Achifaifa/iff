import os
for i in os.listdir('./st')[1:]:exec('from st import '+i[:-3])
cr=c1.a
c=0
while 1:
 os.system('clear')
 if c:print pr[c][1]
 print cr[0],"".join([i[0] for i in cr[1:]]) 
 c=input()
 if c<len(cr):
  pr=cr
  t=pr[1:][c-1]
  cr=eval(t[2]+"."+t[3])

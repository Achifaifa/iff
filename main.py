import os
for i in os.listdir('./story')[1:]:exec('from story import %s'%i[:-3])
cur=chapter1.a1
ch=0
while 1:
 if ch: print pr[1:][ch-1][1]
 os.system('clear')
 print cur[0],"\n","\n".join([i[0] for i in cur[1:]]) 
 try: ch=int(raw_input())
 except KeyboardInterrupt: 1/0
 except: pass
 if ch-1 in range(len(cur[1:])):
  pr=cur
  t=pr[1:][ch-1]
  cur=eval(t[2]+"."+t[3])

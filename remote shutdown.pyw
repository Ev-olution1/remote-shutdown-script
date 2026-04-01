#imports
from requests import get
from time import sleep
from os import system as runcmd

#global const 
Gitlink="https://raw.githubusercontent.com/Ev-olution1/remote-shutdown-script/refs/heads/main/pc_001_state.txt"

#sub procedures

def ReadOnlineRaw(link):
	try:
		onlineRead=get(link)	
		print(onlineRead.status_code)
		state = onlineRead.text
	except: 
		state = 1
	print(str(state))
	return(int(state))
def mainLoop():
	while True:
		state = ReadOnlineRaw(Gitlink)
		if state == 0:
			runcmd("shutdown /r /t 0")
			sleep(10)
		elif state == 1:
			sleep(10)
		print("new cycle")

### start of main procedure
#sleep(15)
mainLoop()
### end of main procedure

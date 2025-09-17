#----------------------------------------------------
import os
import requests
import time
#-------------------------
hostname = ['8.8.8.8','1.1.1.1']
time_pause = 30
#-------------------------
def SendMsgToTelegramChanel(msg):
    token="TOKEN"
    chat_id = 'CHAT_ID'
    params = {'chat_id': chat_id,'text': msg}
    response = requests.get('https://api.telegram.org/bot'+token+'/sendMessage', params=params)
def IsHostAlive(host):
    ret = os.system('ping -c 2 {} > /dev/null'.format(host))
    if ret == 0:
        return True
    return False
while True:
    for i in range(len(hostname)):
        file_signal = hostname[i] +'_down'
        if IsHostAlive(hostname[i]):
            if os.path.isfile(file_signal):
               os.remove(file_signal)
               SendMsgToTelegramChanel(hostname[i] + ' is up')
               #print(hostname + ' is up!')
        else:
            if not os.path.isfile(file_signal):
                open(file_signal,'tw').close()
                SendMsgToTelegramChanel(hostname[i] + ' is down')
                #print(hostname + ' is down!')
    time.sleep(time_pause)
#------------------------------------------------

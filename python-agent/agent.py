import os
import time
import psutil

import json
import requests

mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
mem_gib = mem_bytes/(1024.**3) 
print("Ram Total:",mem_gib) 
print("Cpu Total:",os.cpu_count())

while True:
  cpu_pre=psutil.cpu_percent(os.cpu_count())
  print('The CPU % usage is: ', cpu_pre)
  # load1, load5, load15 = psutil.getloadavg()
 
  # cpu_usage = (load15/os.cpu_count()) * 100
 
  # print("The CPU usage is : ", cpu_usage)
  # Getting % usage of virtual_memory ( 3rd field)
  ram = psutil.virtual_memory()[2]
  print('RAM memory % used:', ram)
  # Getting usage of virtual_memory in GB ( 4th field)
  # print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
  data = {'cpu':cpu_pre,'ram':ram}
  r = requests.post('http://127.0.0.1:3000/api/', json=data)
  print(r)
  time.sleep(0.3)


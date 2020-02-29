"""
Created on Thu Feb 20 13:02:36 2020

@author: iandc
"""

import requests


print('Beginning file download...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
myfile = requests.get(url)
file_location = 'C:/Users/iandc/PythonCode/Data.txt'

#Downloads to: 'C:/VTRoot/HarddiskVolume5/Users/iandc/PythonCode/'

open(file_location, 'wb').write(myfile.content)

with open ('C:/VTRoot/HarddiskVolume5/Users/iandc/PythonCode/Data.txt') as file:
     line = file.readline()
     linenumber = 1
     while line:
      
         #print(f"Request # {linenumber}{line.strip()}")
        
         line = file.readline()
         
         filelines.append(line)
         
         linenumber += 1
         
     test = file.readlines()
     
file.close()

print('File Downloaded')

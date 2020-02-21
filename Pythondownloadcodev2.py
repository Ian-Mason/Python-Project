"""
Created on Thu Feb 20 13:02:36 2020

@author: iandc
"""

import requests


print('Beginning file download...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
myfile = requests.get(url)
file_location = 'F:/School/TCMG - 412/Python Project/Data.txt'

#Downloads to: 'C:/VTRoot/HarddiskVolume5/Users/iandc/PythonCode/'

open(file_location, 'wb').write(myfile.content)

print('File Downloaded')

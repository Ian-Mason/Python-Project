import requests


print('Beginning file download...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
myfile = requests.get(url)
file_location = '/Users/masonbenge/Data.txt'

local = []

remote = []

filelines = []

jan = []
feb = []
mar = []
april = []
may = []
june = []
july = []
aug = []
sep = []
Oct = []
nov = []
dec = []

open(file_location, 'wb').write(myfile.content)

with open ('/Users/masonbenge/Data.txt') as file:
     line = file.readline()
     linenumber = 1
     while line:
         #print(f"Request # {linenumber}{line.strip()}")
         line = file.readline()
         
         filelines.append(line)
         
         linenumber += 1
         
     test = file.readlines()
     
     for i in filelines:
         if i[0:1] == 'l':
             #print (i)
             local.append(i)
         else:
            remote.append(i)
            
     for k in local:
         if k[14:17] == 'Oct':
             Oct.append(k)
         
     
file.close()

print('File Downloaded')

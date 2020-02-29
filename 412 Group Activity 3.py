import requests


print('Beginning file download...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
myfile = requests.get(url)
file_location = '/Users/masonbenge/Data.txt'

local = []

remote = []

filelines = []

failed_req = []

redirected_req = []

most_requested_file = ''

requests_per_day = ''

requests_per_week = ''

requests_per_month = ''

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
         if k[14:17] == 'Jan':
             Oct.append(k)
         if k[14:17] == 'Feb':
             Oct.append(k)
         if k[14:17] == 'Mar':
             Oct.append(k)
         if k[14:17] == 'Apr':
             Oct.append(k)
         if k[14:17] == 'May':
             Oct.append(k)
         if k[14:17] == 'Jun':
             Oct.append(k)
         if k[14:17] == 'Jul':
             Oct.append(k)
         if k[14:17] == 'Aug':
             Oct.append(k)
         if k[14:17] == 'Oct':
             Oct.append(k)
     for i in local:
         for k in i.split():
             if k == '3xx':
                 failed_req.append(i)
     total_requests = len(local)
     
         
     
file.close()

print('File Downloaded\n')
print(f"Total Requests: {total_requests}\n")
print(f"Total 4xx errors: {failed_req}")

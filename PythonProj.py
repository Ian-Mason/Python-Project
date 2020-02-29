from urllib.request import urlretrieve

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
apr = []
may = []
jun = []
jul = []
aug = []
sep = []
Oct = []
nov = []
dec = []



URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'


local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

with open(LOCAL_FILE, 'r') as file:
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
             jan.append(k)
         if k[14:17] == 'Feb':
             feb.append(k)
         if k[14:17] == 'Mar':
             mar.append(k)
         if k[14:17] == 'Apr':
             apr.append(k)
         if k[14:17] == 'May':
             may.append(k)
         if k[14:17] == 'Jun':
             jun.append(k)
         if k[14:17] == 'Jul':
             jul.append(k)
         if k[14:17] == 'Aug':
             aug.append(k)
         if k[14:17] == 'Sep':
             sep.append(k)
         if k[14:17] == 'Oct':
             Oct.append(k)
         if k[14:17] == 'Nov':
             nov.append(k)
         if k[14:17] == 'Dec':
             dec.append(k)
             
             
     for k in remote:
         if k[14:17] == 'Jan':
             jan.append(k)
         if k[14:17] == 'Feb':
             feb.append(k)
         if k[14:17] == 'Mar':
             mar.append(k)
         if k[14:17] == 'Apr':
             apr.append(k)
         if k[14:17] == 'May':
             may.append(k)
         if k[14:17] == 'Jun':
             jun.append(k)
         if k[14:17] == 'Jul':
             jul.append(k)
         if k[14:17] == 'Aug':
             aug.append(k)
         if k[14:17] == 'Sep':
             sep.append(k)
         if k[14:17] == 'Oct':
             Oct.append(k)
         if k[14:17] == 'Nov':
             nov.append(k)
         if k[14:17] == 'Dec':
             dec.append(k)
             
     for i in local:
         for k in i.split():
             if k == '3xx':
                 failed_req.append(i)
     total_requests = len(local)+len(remote)
     
     

jan1 = len(jan)
feb1 = len(feb)
mar1 = len(mar)
apr1 = len(apr)
may1 = len(may)
jun1 = len(jun)
jul1 = len(jul)
aug1 = len(apr)
sep1 = len(sep)
Oct1 = len(Oct)
nov1 = len(nov)
dec1 = len(dec)

total = len(jan)+len(feb)+len(mar)+len(apr)+len(may)+len(jun)+len(jul)+len(apr)+len(sep)+len(Oct)+len(nov)+len(dec)

file.close()

print('File Downloaded\n')

print(f"Total Request in January: {jan1}")
print(f"Total Request in February: {feb1}")
print(f"Total Request in March: {mar1}")
print(f"Total Request in April: {apr1}")
print(f"Total Request in May: {may1}")
print(f"Total Request in June: {jun1}")
print(f"Total Request in July: {jul1}")
print(f"Total Request in August: {aug1}")
print(f"Total Request in September: {sep1}")
print(f"Total Request in October: {Oct1}")
print(f"Total Request in November: {nov1}")
print(f"Total Request in December: {dec1}\n")

print(total, "\n")
print(len(remote), "\n")
print(len(local), "\n")

print(f"Total Requests: {total_requests}\n")
print(f"Total 4xx errors: {failed_req}")

from urllib.request import urlretrieve
from collections import Counter

local = []
remote = []
filelines = []
failed_req = []
redirected_req = []
most_requested_file = ''
requests_per_day = ''
requests_per_week = ''
requests_per_month = ''
resr = []
resl = []
resl2 = []

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
         if k[15:18] == 'Jan':
             jan.append(k)
         if k[15:18] == 'Feb':
             feb.append(k)
         if k[15:18] == 'Mar':
             mar.append(k)
         if k[15:18] == 'Apr':
             apr.append(k)
         if k[15:18] == 'May':
             may.append(k)
         if k[15:18] == 'Jun':
             jun.append(k)
         if k[15:18] == 'Jul':
             jul.append(k)
         if k[15:18] == 'Aug':
             aug.append(k)
         if k[15:18] == 'Sep':
             sep.append(k)
         if k[15:18] == 'Oct':
             Oct.append(k)
         if k[15:18] == 'Nov':
             nov.append(k)
         if k[15:18] == 'Dec':
             dec.append(k)
             
     total_requests = len(local)+len(remote)
     total_req_list = remote + local
     split_elements = []
     
     for i in total_req_list:
         req_split = i.split()
         for k in req_split:
             split_elements.append(k)
     
     def remove_split(x):
         split_elements.remove(x)
         
     for i in split_elements:
         
         if i.isalpha() == True:
             remove_split(i)
         elif i == '-' or '-0600]':
             remove_split(i)
         else:
             if int(i) >= 300:
                 if int(i) >= 400:
                     failed_req.append(i)
                     if int(i) >= 500:
                         failed_req.remove(i)
                         
                 redirected_req.append(i)
                 if int(i) >= 400:
                     redirected_req.remove(i)
         
     
     

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

failed_percent = int()
redirected_percent = int()

print('--------------Data is now being Dissected--------------\n')

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

print(total, "total from dates\n")
print(len(remote), "total from remote\n")
print(len(local), "total from local\n")
################################################

for line in local:        #splits line into types to dissect
    Type = line.split(" ")
    a = Type[1]
    b = Type[2]
    c = Type[3]
    d = Type[4]
    e = Type[5]
    f = Type[6]
    resl.append(f)
    

#for i in remote:       #splits line into types to dissect 
    #Type = i.split(" ")
    #g = Type[1]
    #h = Type[2]
    #i = Type[3]
    #j = Type[4]
    #k = Type[5]
    #l = Type[6]
    #resr.append(f)


resl2 = [(k,v) for k,v in Counter(resl).items() if v > 5000]  #finds most accessed
resl2.sort(key=lambda kv: kv[1])
resl2 = [k for k,v in resl2]

resl3 = [(x,t) for x,t in Counter(resl).items() if t <= 1]  #finds least accessed
resl3.sort(key=lambda xt: xt[1])
resl3 = [x for x,t in resl3]


print(len(resl), "Local file name total\n")
print(len(resr), "Remote file name total\n")




##############################################
print(f"The File that is most accessed is: {resl2[0]}\n")   #only for local
print(f"The File that is least accessed is: {resl3[0]}\n")  #only for local
print(f"Total Requests: {total_requests}\n")
print(f"4xx Error %: {failed_percent}\n")
print(f"3xx Error %: {redirected_percent}\n")


file.close()
print("--------------Data Dissected--------------")
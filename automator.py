import os
import random
from time import sleep
import argparse
import urllib3
import json
from time import sleep
import csv
import datetime

startTime = datetime.datetime.now()

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Instagram Username")
parser.add_argument("password", help="Instagram Password")
args = parser.parse_args()
urllib3.disable_warnings()


print("ENDGAME - INSTRAGRAM DIRECT MESSAGES DUMPER")

print("thread list generating ...\n")

os.system('python threads.py -u {0} -p {1} > threads'.format(args.username,args.password))
print("thread list generated\n")

list_dirs = os.listdir("./output/")


fn = open("listthreads","r")
print("reading from threadlist\n")

fnf = fn.readlines()
for i in fnf:
    thread = i.strip()
    if thread in list_dirs:
        continue
    else:
        print(thread)
        os.system('python main.py -u {1} -p {2} -t {0} -o ./output/{0}'.format(thread,args.username,args.password)) #already creates a folder itself
        randomn = random.randint(10,20)
        print("random sleep for {0} seconds".format(randomn))
        sleep(randomn)
print("dump finished")        
print("CONVERTING PHASE")

list_dirs = os.listdir("./output/")
http = urllib3.PoolManager()


print(list_dirs)
user_infos = []
temp_usr = []
sleep(10)
for d in list_dirs:
    print(d)
    if d == ".DS_Store":
        continue
    result = ""
    with open("./output/"+d+"/dump_file.csv","r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=' ', quotechar='|')
        with open("./output/"+d+"/results.csv", mode='w') as csv_w:
            fieldnames = ['userid', 'username', 'fullname', 'message', 'date']
            writer = csv.DictWriter(csv_w, fieldnames=fieldnames)
            writer.writeheader()
            for row in csv_reader:
                if row['message'].strip() in ["reel_share","media_share",""," ","action_log","link"] :
                    continue
                username ="private"
                full_name ="private"
                userid = row['userid']
                if userid not in temp_usr:
                    if userid.isdigit():
                        #print("CALLING FOR ", userid)
                        r = http.request('GET',"https://i.instagram.com/api/v1/users/{0}/info/".format(userid))
                        #print(r.data)
                        u = json.loads(r.data.decode('utf-8'))
                        user_infos.append([userid,u['user']['username'],u['user']['full_name']])
                        temp_usr.append(userid)
                for us in user_infos:
                    if us[0] == userid:
                        username = us[1]
                        full_name = us[2]
                writer.writerow({'userid': userid, 'username': username, 'fullname': full_name, 'message': row['message'], 'date': row['date']})

endTime = datetime.datetime.now()
print("started at: {0} ended at: {1}".format(startTime,endTime)) 


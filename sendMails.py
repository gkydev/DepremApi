import requests, time, os
from datetime import datetime
from resources import split_data,get_message
print("Started.. \n")
basedir = os.path.abspath(os.path.dirname(__file__))
filedir = basedir + "/lastErtq.txt"
stmtime = os.stat(filedir).st_mtime
mailaddy = "YOUR MAIL ADDY"
apilink = "YOUR MAILGUN API LINK"
secretkey = "YOUR MAILGUN SECRETKEY"
def check_isbigenough(data):
    buyukluk = float(data["buyukluk"])
    if buyukluk >= 3.5:
        return True
    else:
        return False
def send_mail(sendto,message):
    r = requests.post(
        apilink,
        auth=("api",secretkey),
        data={"from": mailaddy,
            "to": [sendto],
            "subject": "Deprem Bildirimi",
            "html": message})
    return print(r.text)
def is_updated(stmtime):
    if stmtime == os.stat(filedir).st_mtime:
        print("Nothing changed")
        return stmtime
    else:
        with open("sublist.txt","r") as fp:
            lines = fp.readlines()
            fp.close()
        with open("lastErtq.txt","r") as fp:
            Ertq = fp.readline()
            fp.close()
        data = split_data(Ertq)
        isbigenough = check_isbigenough(data)
        message = get_message(data)
        if isbigenough == True:
            print("Updated sending mails...")
            with open("send_mail.log","a") as fp:    
                for line in lines:
                    sendto = line.strip("\n")
                    print("Sending to : " + sendto)
                    fp.write(sendto + "     " + str(datetime.now()) + "\n")
                    send_mail(sendto,message)
                fp.close()
        elif isbigenough == False:
            print("Updated but not high enough passing.")   
        else:
            pass
        return os.stat(filedir).st_mtime
while True:
    print("Checking updates.. | " + time.asctime())
    stmtime = is_updated(stmtime)
    time.sleep(50)
    

# -*- coding: utf-8 -*-
import os, sys, requests, time
from bs4 import BeautifulSoup as bs
import difflib
def get_lastErtq():
    try:
        source = requests.get("http://www.koeri.boun.edu.tr/scripts/lst6.asp")
        soup = bs(source.text,'html.parser')
        depremler = soup.find("pre")
        cleaned = depremler.text.strip("<pre>").strip("</pre>")
        splitted = cleaned.split("\n")
        final = splitted[7].replace("Ý","i")
        # log 
        with open("log.txt","a") as fp:
            fp.write("Grabbed time : " + time.asctime() + "\n")
            fp.write("------------------------------------- \n")
            fp.write(final + "\n")
            fp.write("\n")
            fp.close()
        print(final)
        return final
    except Exception as e:
        with open("errors.txt","a") as fp:
            fp.write("Error time : " + time.asctime() + "\n")
            fp.write("Error : " + str(e) + "\n")
            fp.write("Error File : deprem-grabber.py \n")
            fp.write("--------------------- \n")
            fp.close()
        return False
def check_Ertq():
    newErtq = get_lastErtq()
    while newErtq == False:
        newErtq = get_lastErtq()  
    newErtq = newErtq.strip("\n")
    with open("lastErtq.txt","r",encoding="windows-1252") as fp:
        Ertq = fp.readline()
        with open("toremove.txt","w") as fp:
            fp.write(newErtq)
            fp.close()
        with open("toremove.txt","r") as fp:
            newErtq = fp.readline()
            fp.close()
        print(Ertq)
        fp.close()
    if Ertq == newErtq:
        pass
    elif Ertq != newErtq:
        with open("lastErtq.txt","w") as fp:
            fp.write(newErtq)
            fp.close()
while True:
    check_Ertq()
    time.sleep(60)
    

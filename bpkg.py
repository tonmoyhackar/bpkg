import os, sys, time
from time import sleep
rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
def ani(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def logo ():
  os.system("clear")
  os.system("""echo '  
   _______ ____  _   _ __  __  ______     __
 |__   __/ __ \| \ | |  \/  |/ __ \ \   / /
    | | | |  | |  \| | \  / | |  | \ \_/ / 
    | | | |  | | . ` | |\/| | |  | |\   /  
    | | | |__| | |\  | |  | | |__| | | |   
    |_|  \____/|_| \_|_|  |_|\____/  |_|   
  ╔════════════════════════════════════════════════╗
  ║            [✓] TOOL NAME : BPKG                ║
  ║            [✓] GITHUB : Tonmoy-Toxic           ║
  ║            [✓] FACEBOOK : TONMOY.HASAN88       ║
  ║            [✓] TELEGRAM : Tonmoy Thech               ║
  ║            [✓] INSTAGRAM : Tonmoy              ║
  ║            [✓] EMAIL : tonmoytoxicyt@gmail.com        ║
  ╚════════════════════════════════════════════════╝\n----------------------------------------------------'|lolcat""")
  ani(r+"\t<"+bl+"p"+r+">"+g+" MAKE GOOGLE YOUR BEST FRIEND :) "+r+"<"+bl+"/p"+r+">")
  os.system("echo '----------------------------------------------------'| lolcat")
  
logo ()
def main ():
  
  x = input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m PRESS ANY KEY FOR START\033[1;0;40m")
  logo ()
  os.system('''termux-setup-storage
yes | pkg update 
yes | pkg upgrade 
yes | pkg install python 
yes | pkg install python2 
pip3 install pip requests mechanize beautifulsoup4 infocircle myspeed 
pip2 install pip requests mechanize beautifulsoup4
pip install --upgrade pip
yes | pkg install fish 
yes | pkg i zsh 
yes | pkg install ruby 
yes | pkg install git 
yes | pkg install php 
yes | pkg install perl 
yes | pkg install nmap 
yes | pkg install bash 
yes | pkg install clang 
yes | pkg install nano 
yes | pkg install w3m 
yes | pkg install figlet 
yes | pkg install cowsay 
yes | pkg install curl 
yes | pkg install tar 
yes | pkg install zip 
yes | pkg install unzip 
yes | pkg install tor 
yes | pkg install wget 
yes | pkg install wireshark 
yes | pkg install wgetrc 
yes | pkg install wcalc 
yes | pkg install bmon 
yes | pkg install unrar 
yes | pkg install toilet 
yes | pkg install proot 
yes | pkg install net-tools 
yes | pkg install golang 
yes | pkg install chroot 
yes | pkg install macchanger 
yes | pkg install openssl 
yes | pkg install cmatrix 
yes | pkg install openssh 
yes | pkg install wireshark 
yes | pkg install macchanger 
yes | pkg install nano
yes | pkg install nmap
yes | pkg install clang
yes | pkg install bash
yes | pkg install proot
yes | pkg install vim
yes | pkg install net-tools''')
  print("\t\033[1;30;40m[\033[1;34 ;40m+\033[1;30;40m]\033[1;32;40m INSTALLED PKG SUCCESSFUL \033[1;0;40m")
  logo ()
  pkg = input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m SEE INSTALLED PKG [Y/N] : \033[1;39;40m")
  if pkg == "y" or pkg == "Y":
    os.system("pkg list-installed")
  else:
    sys.exit ()
if __name__=='__main__':
  main ()
 
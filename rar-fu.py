########################################################
# Do not work on Pydroid 3 because it needs unrar package to unlock rarfiles #
# If you use termux – you are good to go                                                                 #
########################################################

import os, time
import rarfile #needs unrar pkg
from termcolor import colored

# font-colors
class fontcolor():
	def green(string):
		return colored(string, "green", attrs=['bold'])
	def light_green(string):
		return colored(string, "green")
	def white(string):
		return colored(string, "white", attrs=['bold'])
	def yellow(string):
		return colored(string, "yellow", attrs=['bold'])
	def cyan(string):
		return colored(string, "cyan", attrs=['bold'])
	def red(string):
		return colored(string, "red", attrs=['bold'])
	def blue(string):
		return colored(string, "blue", attrs=['bold'])

# smb ==> symbols
class smb:
	WARN = fontcolor.red("[-] ")
	DONE = fontcolor.green("[+] ")
	INPUT = fontcolor.cyan("[»] ")
	INFO = fontcolor.yellow("[!] ")

# banner art
banner_1 = fontcolor.light_green('''
      ██▀███   ▄▄▄       ██▀███       █████▒█    ██ 
     ▓██ ▒ ██▒▒████▄    ▓██ ▒ ██▒   ▓██   ▒ ██  ▓██▒
     ▓██ ░▄█ ▒▒██  ▀█▄  ▓██ ░▄█ ▒   ▒████ ░▓██  ▒██░
     ▒██▀▀█▄  ░██▄▄▄▄██ ▒██▀▀█▄     ░▓█▒  ░▓▓█  ░██░
     ░██▓ ▒██▒ ▓█   ▓██▒░██▓ ▒██▒   ░▒█░   ▒▒█████▓ 
     ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░    ▒ ░   ░▒▓▒ ▒ ▒ 
       ░▒ ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░    ░     ░░▒░ ░ ░ 
       ░░   ░   ░   ▒     ░░   ░     ░ ░    ░░░ ░ ░ 
        ░           ░  ░   ░                  ░     
                                               ''')
banner_2 = fontcolor.white('''                  GitHub : @sumit-buddy''')
banner_3 = fontcolor.green('''     -----------------------------------------------''')
banner_4 = fontcolor.green('''       || Rar-Fu : RAR file dictionary attacker ||''')
banner_5 = fontcolor.green('''     -----------------------------------------------''')

# print banners
def banner():
	print(banner_1)
	print(banner_2)
	print(banner_3)
	print(banner_4)
	print(banner_5)
	
# shows start time
def start_time():
	start_time_show = time.asctime()
	print(fontcolor.green("\nStart time ==> ") + fontcolor.white(start_time_show) + "\n")

# shows end time
def end_time():
	end_time_show = time.asctime()
	print(fontcolor.green("\nEnd time ==> ") + fontcolor.white(end_time_show) + "\n")

# check path and file
def check_path(path):
    if os.path.isfile(path):
    	pass
    else:
    	print(f"{smb.WARN}File Not Found !")
    	exit()

# count password from text file
def count_passwd(text_file):
        count = 0
        with open(text_file, "r") as wordlist:
            for line in wordlist:
                count += 1
        return count

# clear screen
def clr_scr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

# use unrar to unlock rar file
def unrar(passwd, rar_file):
	fileload = rarfile.RarFile(rar_file)
	fileload.UNRAR_TOOL = "UnRAR.exe"
	fileload.extractall("cracked_files", pwd = passwd)

# try passwords from wordlist
def crack():
	passfile = open(pass_file, "r")
	passwords = passfile.readlines()
	for passwd in passwords:
		passwd = passwd.rstrip("\n")
		try:
			unrar(passwd, rar_file)
			print(f"\n{smb.DONE}" + fontcolor.green("PASSWORD FOUND & FILE CRACKED : ") + fontcolor.white(passwd))
			break
		except:
			print(f"{smb.WARN}Wrong Password : " + passwd)

while True:
	banner()
	rar_file = input(f"\n{smb.INPUT}" + fontcolor.white("Enter Rar File Path : "))
	check_path(rar_file)
	pass_file = input(f"{smb.INPUT}" + fontcolor.white("Enter Password List Path : "))
	check_path(pass_file)
	total_passwds = count_passwd(pass_file)
	print(f"\n{smb.DONE}" + fontcolor.white("Total Passwords In Wordlist : ") + fontcolor.green(total_passwds))
	print(f"\n{smb.DONE}" + fontcolor.white("Starting Cracking ") + fontcolor.green(rar_file))
	time.sleep(4)
	start_time()
	start_time = time.time()
	crack()
	end_time()
	print(fontcolor.green("Program Executed In ==> ") + fontcolor.white("%s seconds") % (time.time() - start_time))
	input("\nPress [ENTER] To Continue...")
	clr_scr()
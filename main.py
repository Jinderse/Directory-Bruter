import requests
from colorama import Fore
import platform
info = platform.uname()[0]
if info == "Windows":
    exit("Windows users cannot use this tool")
else:
    pass
try:
    
    dirin = input(Fore.CYAN+"Enter dirlist : ")

    dirlist = open(dirin).read().split()
    print(Fore.YELLOW+"https://web name/")
    url = input(Fore.YELLOW+"Enter Your URL : ")
    
    for i in dirlist:
        http = requests.get(url+i).status_code
        if http == 200:
            print(Fore.GREEN+" [+] There is >>>>> "+i)
            break
        
        else:
            print(Fore.RED+"[-] Does not exist >>>>>> "+i)
        
    
except FileNotFoundError:
    print("please Enter valid dyrectory list")
except requests.exceptions.MissingSchema:
    print("please Enter valid URL")

import socket
import time
from colorama import Fore, init




init(autoreset=True)

print(Fore.RED + "THIS PORT TESTER WAS MADE BY @REDSIMIT")
ip = input( Fore.GREEN + "Input the following ip adress: ")
port = int(input(Fore.GREEN + "Input the following port: "))
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "Connecting...")
time.sleep(2)

try:
    socket.create_connection((ip, port), timeout=3)
    print(Fore.GREEN + "port is open")
except socket.error:
    print(Fore.GREEN + "port is closed")
print(Fore.RED + "More Tools in https://Redsimit.netlify.app")






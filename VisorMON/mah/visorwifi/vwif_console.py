from vx.headh import *
import time
import subprocess

while True:
    cons= input("> ")

    if cons.lower() == 'exit':
        print()
        print(f"       {Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Lacze z {Fore.RED}VisorForce{Fore.WHITE}")
        print()
        time.sleep(2)
        print("\033c", end='')
        print(h1)
        time.sleep(2)
        print(h2)
        print(hinfo)
        break


    elif cons.lower() == 'ping':

        print(f"Pong {username}")

    elif cons.lower() == 'clear':
        print("Clear")
        print("\033c", end='')
        time.sleep(2)
        print(h3)




    elif cons.lower() == f'{com_prx}help' or cons.lower() == 'help' :

        print(vwifihelp)




    else:
        print()
        print(f"    Sprobuj urzyc {Fore.CYAN}{com_prx}help{Fore.WHITE} :Q")
        print()
from vx.headh import *
from vx.source import *
import time
import subprocess

while True:
    cons= input("> ")

    if cons.lower() == 'exit':
        print()
        print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Exit Init")
        print()
        time.sleep(2)

        break  # Przerwij pętlę


    elif cons.lower() == 'ping':

        print(f"Pong {username}")
        print(h6)

    elif cons.lower() == 'clear':
        print("Clear")
        print("\033c", end='')
        print(h1)
        time.sleep(2)
        print(h2)
        print(hinfo)




    elif cons.lower() == f'{com_prx}help' or cons.lower() == 'help' :

        print(help)


    elif cons.lower() == f'{com_prx}vwifi' :

        from mah.visorwifi.vwif_init import *


    elif cons.lower() == '4' or cons.lower() == f'{com_prx}venc':
        print(f"    visorDCD.exe {Fore.GREEN}is running{Fore.WHITE} Using (" + cons + ")")
        subprocess.run(visord)
        print()
        print(f"    visorDCD.exe {Fore.RED}is stopped{Fore.WHITE}")
        print()


    else:
        print()
        print(f"    Sprobuj urzyc {Fore.RED}{com_prx}help{Fore.WHITE} ;D")
        print()
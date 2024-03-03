import requests
import time
from vx.colors import *
from vx.lgs import *

def pobierz_zawartosc_pastebin(url_pastebin):
    odpowiedz = requests.get(url_pastebin)

    if odpowiedz.status_code == 200:
        return odpowiedz.text
    else:
        print(f"Błąd pobierania z Pastebin. Kod błędu: {odpowiedz.status_code}")
        return None

def sprawdz_logowanie(login, haslo, dane_logowania):
    return login in dane_logowania and dane_logowania[login] == haslo

if __name__ == "__main__":
    test = "Cpk0HY7K"
    url_pastebin = f"https://pastebin.com/raw/{test}"

    zawartosc_pastebin = pobierz_zawartosc_pastebin(url_pastebin)

    if zawartosc_pastebin:
        linie = zawartosc_pastebin.split('\n')
        dane_logowania = {}

        poprawne_logowanie = False 

        for i in range(0, len(linie), 2):  
            login = linie[i].strip()
            haslo = linie[i + 1].strip()
            dane_logowania[login] = haslo

            login_test = login_l
            haslo_test = login_p

            if sprawdz_logowanie(login_test, haslo_test, dane_logowania):
                print("\033c", end='')
                print()
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}Zalogowano pomyślnie jako{Fore.RED} █ {login_test} █{Fore.WHITE}. :DDD")
                print()
                print(f"     Ładowanie {Fore.RED}VisorForce {Fore.WHITE}")
                time.sleep(3)
                with open('vx/lastlogin.txt', 'w') as file:
                    file.write(login_test)
                from vx.init import *
                poprawne_logowanie = True
                break

        if not poprawne_logowanie:
            print()
            print(f" {Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Nie poprawna nazwa urzytkownika lub haslo . :P")
            time.sleep(3)
    else:
        print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Sprawdź połączenie z internetem.")
        time.sleep(3)


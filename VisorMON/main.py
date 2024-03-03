import subprocess


def uruchom_inny_plik(nazwa_pliku):
    try:
        subprocess.run(['python', nazwa_pliku], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Błąd podczas uruchamiania pliku: {e}')

if __name__ == "__main__":
    nazwa_pliku_do_uruchomienia = 'pasch.py'  # Zmodyfikuj nazwę pliku na właściwą

    uruchom_inny_plik(nazwa_pliku_do_uruchomienia)

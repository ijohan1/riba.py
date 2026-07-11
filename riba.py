import pandas as pd
from pathlib import Path
import statistics
from collections import Counter

print("""           FISHKISSFISHKIS
       SFISHKISSFISHKISSFISH            F
    ISHK   ISSFISHKISSFISHKISS         FI
  SHKISS   FISHKISSFISHKISSFISS       FIS
HKISSFISHKISSFISHKISSFISHKISSFISH    KISS
  FISHKISSFISHKISSFISHKISSFISHKISS  FISHK
      SSFISHKISSFISHKISSFISHKISSFISHKISSF
  ISHKISSFISHKISSFISHKISSFISHKISSF  ISHKI
SSFISHKISSFISHKISSFISHKISSFISHKIS    SFIS
  HKISSFISHKISSFISHKISSFISHKISS       FIS
    HKISSFISHKISSFISHKISSFISHK         IS
       SFISHKISSFISHKISSFISH            K
         ISSFISHKISSFISHK               """)

print("привіт! я твій помічник для перегляду параметрів за файлами баз даних. сподіваюся бути корисним :) ")

def opening():
    while True:
        pith=Path(input("вкажи шлях папки з файлами у форматі /шлях/до/папки: "))
        if pith.exists() and pith.is_dir():
            print("знайшов таке!\n,")
            return pith
        else:
            print("не бачу... ще разок: ")




def getfilez(pith):
    filez = []

    for file in pith.iterdir():
        if file.suffix in [".csv", ".txt"]:
            filez.append(file)

    if filez:
        print("доступні файли у твоїй папочці: ")
        for i, f in enumerate(filez): print(f"{i+1}. {f.name}")
        return filez
    else: print("не бачу файликів. спробуй закинути у вказану тобою папку файли у форматі .csv або .txt і спробуй знову!")
    return[]


def chose(filez):
    while True:
        numba=input("який файлик береш для аналізу?\n")

        if numba.isdigit():
            numb = int(numba)

            if 1 <=  numb <= len(filez):
                file = filez[numb - 1]
                print("чудово, відкриваю...\n")
                return file

            else: print("такого файла нема.. спробуй ще:")
        else: print("файл має вказатися числом: ")

def view(file):
    if file.suffix == ".csv":
        view1 = pd.read_csv(file)
        return f"зміст вибраного тобою файла:\n {view1.to_string()}\n"
    elif file.suffix ==  ".txt":
        with open(file, "r") as vview2:
           view2 = vview2.read()
        return f"зміст вибраного тобою файла:\n {view2}\n"
    else: return "дивний формат.. я такого відкривати ще не вмію :( )"


def operata(file): #ця функція досить примітивна і рахує все правильно лише коли у файлів по одному рядкові даних. для текстового файлу треба, аби числа всередині просто були написані через кому. покращення будуть згодом

    if file.suffix == ".csv":
        panda = pd.read_csv(file, header=None)
        pinda=panda.iloc[0]
        if pinda.empty: return "ой, схоже, файл порожній або в ньому нема чого аналізувати. це точно числовий файлик?"

        mode=pinda.mode()
#        if not modes.empty: mode=modes.iloc[0]
#        else: mode = "за файлом не знайдено моди.."
        median=pinda.median()
        mean=pinda.mean()

        return f"по .csv файлові порахував наступне:\nмода: {mode}\nмедіана: {median}\nсереднє: {mean}"

    elif file.suffix == ".txt":
        with open(file, "r") as f:
            filik=f.read().strip()

            lines=filik.splitlines()
            data=[]
            for line in lines: data.extend(map(float, line.split(",")))
            s=pd.Series(data)

            moda= s.mode()[0]
            mediana=s.median()
            seredne=s.mean()

            return f"по .txt файлові порахував наступне:\nмода: {moda}\nмедіана: {mediana}\nсереднє: {seredne}"

def main():
    pith = opening()
    if pith is None: return
    filez = getfilez(pith)
    if not filez: return

    file = chose(filez)
    print(view(file))
    print(operata(file))

main()
print("готово! звертайся, коли треба допомога ще :)")

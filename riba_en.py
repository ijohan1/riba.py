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

print("hi! I'm your dataset wizard.I can view various parameters regarding to your file of choice. glad to help ya :) ")

def opening():
    while True:
        pith=Path(input("tell me the name of your folder /somehow/like/this: "))
        if pith.exists() and pith.is_dir():
            print("got it!\n,")
            return pith
        else:
            print("not getting it... one more time: ")




def getfilez(pith):
    filez = []

    for file in pith.iterdir():
        if file.suffix in [".csv", ".txt"]:
            filez.append(file)

    if filez:
        print("available files in your folder: ")
        for i, f in enumerate(filez): print(f"{i+1}. {f.name}")
        return filez
    else: print("can't see any files. try to create some files here with .csv or .txt format and try again!")
    return[]


def chose(filez):
    while True:
        numba=input("gimme the number of file you wanna open today: \n")

        if numba.isdigit():
            numb = int(numba)

            if 1 <=  numb <= len(filez):
                file = filez[numb - 1]
                print("aight, working on it...\n")
                return file

            else: print("there is no such file.. come again: ")
        else: print("i need a number: ")

def view(file):
    if file.suffix == ".csv":
        view1 = pd.read_csv(file)
        return f"your file:\n {view1.to_string()}\n"
    elif file.suffix ==  ".txt":
        with open(file, "r") as vview2:
           view2 = vview2.read()
        return f"your file:\n {view2}\n"
    else: return "weird formatting.. I dunno how to open these yet :( )"


def operata(file): #ця функція досить примітивна і рахує все правильно лише коли у файлів по одному рядкові даних. для текстового файлу треба, аби числа всередині просто були написані через кому. покращення будуть згодом

    if file.suffix == ".csv":
        panda = pd.read_csv(file, header=None)
        pinda=panda.iloc[0]
        if pinda.empty: return "woopsie, your file is empty. are u sure this is the correct one?"

        mode=pinda.mode()
#        if not modes.empty: mode=modes.iloc[0]
#        else: mode = "за файлом не знайдено моди.."
        median=pinda.median()
        mean=pinda.mean()

        return f"calculated results on your .csv file:\nmode: {mode}\nmedian: {median}\nmean: {mean}"

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

            return f"calculated results on your .txt file:\nmode: {moda}\nmedian: {mediana}\nmean: {seredne}"

def main():
    pith = opening()
    if pith is None: return
    filez = getfilez(pith)
    if not filez: return

    file = chose(filez)
    print(view(file))
    print(operata(file))

main()
print("done! come back any time :)")

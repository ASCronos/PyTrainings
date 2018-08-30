#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Adam Cronos"
__license__ = "GPL"
__version__ = "1.1"

import string
import sys
import os

print ("============================================================")
print ("Za chwile wygenerujesz tablice znakow o zadanych wymiarach\n\
i zdefiniowanej zawartosci (litery, cyfry, znaki specjalne).\n\
Teraz podasz potrzebne parametry.")
print ("============================================================")

def tablica():
    "Funkcja losuje tablicę znaków o zadanych wymiarach, z podanej puli. "
    import random
    out_file = open('tablica.txt', 'w')
    
    x = int(input("\nPodaj liczbe znakow w wierszu: "))
    y = int(input("Podaj liczbe wierszy: "))
    char_set = input("Podaj zawartosc tablicy wg wzoru: \n\
     A+a+c+z\n\
     gdzie:\n\
      A - duze litery A-Z\n\
      a - male litery a-z\n\
      c - cyfry 0-9\n\
      z - znaki specjalne\n\
      hex - znaki szesnastkowe 0-9, A-F\n")

    A = string.ascii_uppercase
    a = string.ascii_lowercase
    c = string.digits
    z = string.punctuation
    hex = str.upper(string.hexdigits)

    decyzja = input("Czy chcesz oddzielac elementy wiersza spacjami aby zwiekszyc czytelnosc tablicy?\n\
(niezalecane jesli chcesz bezposrednio kopiowac wiersze jako hasla)\n\
[y/n] ")
    if decyzja == "y":
        separator = ' '
    else:
            separator = ''

    for i in range(y):
        wiersz = (separator.join(random.sample(eval(char_set), x)))
        print (wiersz)
        out_file.write(wiersz + '\n')
    print("\n")
    print ("Oto wygenerowana tablica.\n\
Zostala ona zapisana w pliku tablica.txt w folderze programu.\n")
    print
    os.system("pause")

# Główna część programu
try:
    tablica()
except ValueError: 
    print ("Pula znakow jest zbyt mala. Zmniejsz dlugosc wiersza lub zwieksz pule.")
    tablica()
except:
    print ("Wystapil blad. Program zakonczy dzialanie."), sys.exc_info()[0]
    raise

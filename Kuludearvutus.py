# Programm võimaldab kasutajal sisestada jooksvalt oma kulutusi, talletada need tekstifaili
# Saada peale kulude sisestamist teada kulutatud summa kokkuarvutatult

from easygui import *
import sys  
import re


# Eeldame, et kasutaja sisestab kulu liigi ja kulu täisarvuna, nt "Vesi 13"
# Kulu liik on vajalik eelkõige kasutaja jaoks, kui ta soovib hiljem tekstifaili kasutada

while True:
    kulutused = enterbox("Sisesta kulud:") # lahter kulude sisestamiseks
    
    f = open("kulud.txt", "a", encoding="UTF-8") # Ava fail, kui seda pole, siis loo sellenimeline
    f.write(kulutused + "\n") # Kirjuta sisestatud kulutused faili eraldi ridadele
    with open('kulud.txt', encoding="UTF-8") as f: # Loe sisestatud numbrid ja liida kokku
        fdata = f.read()  # Kood mooduliga re lehelt stackoverflow.com; loeb andmed failist
        reObj = re.compile('\d+\.\d+|\d+')   # Määrab mooduli numbreid otsima
        mo = reObj.findall(fdata)   # Leiab numbrid
        n = [] # Loob tühja listi numbrite jaoks
        for i in mo:n.append(float(i)) # Lisab leitud numbrid listi
    f.close() # Sulgeme faili
    
    msg = "Kas soovid jätkata?"
    if ccbox(msg, choices = ("OK", "Cancel")):    # Vali kas jätkata kulude sisestamist või mitte
        pass  # Kasutaja soovib jätkata kulude sisestamist
    else:
        teade = msgbox("Sinu kulud kokku: " + str(sum(n)) + " eurot") # Väljastab kulud kokku      
        sys.exit() # Lõpetab programmi töö
        


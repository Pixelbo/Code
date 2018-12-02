import string
import random


stat = list(string.printable)
nbpioche = []
pioche = []
         
#demander le mot crypter ou pas crypter
def mott():
    Mot = input("Mot: ")
    return Mot

#demander la clé pour le decryptage
def clle():
    Cle = input("la cle(chiffres): ")

    Cle2 = Cle.replace(",", "")
    Cle3 = Cle2.replace("[", "")
    Cle4 = Cle3.replace("]", "")
    Cle5 = Cle4.split()

    return Cle5

#séparer chaque lettre du mot dans une list
def sliceMot(mot):
    motslice = list(mot)
    return motslice;


#définir la clé( ou l'alphabet en num d'id)
def nbpioch():
    i=0
    
    def re():
        nb = random.randint(0, 99)
        if not nb in nbpioche:
            nbpioche.append(nb)
        else:
            re()
            
    while not i==100:
        re()
        i += 1

#Convertir la clé ( ou l'alphabet en num d'id) en alphabet char
def pioch():
    j=0
    while not j==100:
        pioche.append(stat[nbpioche[j]])
        j += 1

#Convertir la clé ( ou l'alphabet en num d'id) en alphabet char mais pour décrypt
def depioch(self):
    j=0
    while not j==100:
        pioche.append(stat[int(self[j])])
        j += 1


#utiliser le mot découper et la clé pour en faire un mot crypter
def finalcountdown(motslice):
    final = []
    k = 0
    while not k == len(motslice):
        word = motslice[k]
        wordd = stat.index(word)
        final.append(pioche[wordd])
        k+=1
    return final

#groupe la list du mot crypt(en lettre détacher) en string
def group(fibal):
    l=0
    finalgroup=""
    while not l == len(fibal):
        finalgroup = finalgroup+fibal[l]
        l+=1
    return finalgroup

#utiliser le mot découper et la clé pour en faire un mot decrypter (l'inverse)
def decrypt1(motslic):
    final = []
    m = 0
    while not m == len(motslic):
        word = motslic[m]
        wordd = pioche.index(word)
        final.append(stat[wordd])
        m+=1
    return final
        
    
    
        
#crypt étapes#
def crypt(mot):



    motslice = sliceMot(mot)

    nbpioch()

    pioch()

    final = finalcountdown(motslice)

    finalgroup = group(final)

    print(finalgroup)
    
    print("cle a sauvgarder:")
    print(nbpioche)

    return finalgroup, nbpioch

#decrypt étapes#
def decrypt(mot2, nbpioche3):
    
    motslice = sliceMot(mot2)
    
    depioch(nbpioche3)
    
    final = decrypt1(motslice)
    
    finalgroup = group(final)
    
    print(finalgroup)


#choisis entre crypt et décrypt pour fair non-directement(pas faire crypt(mot)
def choose():
    chose = input("crypt(1) ou decrypt(2): ")
    if chose == "1":
        mot2 = mott()
        crypt(mot2)
    elif chose == "2":
        nbpioche3 = clle()
        mot = mott()
        decrypt(mot, nbpioche3)
    else:
        choose()














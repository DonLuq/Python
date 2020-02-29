#!/usr/bin/env python3
import zipfile
import networkx as nx
import matplotlib.pyplot as plt
import sys, os
from urllib.parse import quote, unquote
import os.path as PATH


def TXYZ_tuple(old_xyz):
    'funkcja przyjmujaca plik w formacie txt/xyz i dajaca jako rezultat liste w formie [Typ,x,y,z]'
    u = open(str(source_zip)+'/'+str(old_xyz),'r')
    new_xyz = []
    while 1:
        l=u.readline()
        if l == '':
            break
        if len(l)>4:
            wsp=l.split()
            new_xyz.append([wsp[0]] + list(map(float, wsp[1:])))
    return(new_xyz)



def wypisz_do_pliku(xyz,name='PLIK',AB = 2):
    'funkcja przyjmujaca jako argument format [tyxz,nazwe,typ] i tworzaca na podstawie niego pliki z rozszerzeniem .inp'
    NAME = name.split('.')
    #metoda = ['AM1', 'HF-3c', 'B97-D3 def2-SVP def2/J', 'RI B97-3c'] 
    #metoda = ['RI-SCS-MP2 def2-TZVP def2-TZVP/C', 'RI-SCS-MP2 def2-SVP def2-SVP/C', 'RI-SCS-MP2 def2-TZVPP def2-TZVPP/C', 'RI-SCS-MP2 def2-QZVPP def2-QZVPP/C']
    #metoda = ['HF-3c', 'HF def2-TZVP', 'MP2 def2-TZVP', 'RI-SCS-MP2 def2-TZVP def2-TZVP/C', 'RIJK SCS-MP3 def2-TZVP def2/JK def2-TZVP/C', 'RI-CCSD def2-TZVP def2-TZVP/C', 'RI-CCSD(T) def2-TZVP def2-TZVP/C', 'RI LSD def2-TZVP def2/J', 'RI PW91 D3 def2-TZVP def2/J','RIJK B97-D3 def2-TZVP def2/J', 'B3LYP RIJONX','RI M06L def2-TZVP def2/J','RIJK PWPB95 D3BJ def2-TZVP def2/JK def2-TZVP/C','PWPB95']
    #metoda = ['HF-3c', 'HF def2-TZVP','MP2 def2-TZVP','RI-SCS-MP2 def2-TZVP def2-TZVP/C', 'RIJK SCS-MP3 def2-TZVP def2/JK def2-TZVP/C','RI-CCSD def2-TZVP def2-TZVP/C', 'RI-CCSD(T) def2-TZVP def2-TZVP/C']
    metoda = ['RI LSD def2-TZVP def2/J', 'RIJK B97-D3 def2-TZVP def2/J', 'B3LYP RIJONX','RI M06L def2-TZVP def2/J','RIJK PWPB95 D3BJ def2-TZVP def2/JK def2-TZVP/C','PWPB95']
    for i in range(len(metoda)):
        TYP = ['_A','_B','_AB']
        PLIK=open(NAME[0] +"_"+ quote(metoda[i],safe='') + TYP[AB] + '.inp','w+')
        PLIK.write("! {}\n%pal nprocs 1\nend\n* xyz 0 1\n".format(metoda[i]))

        for i in range(len(xyz)):
            PLIK.write("{0} {1} {2} {3}\n".format(str(xyz[i][0]),str(xyz[i][1]),str(xyz[i][2]),str(xyz[i][3])))
        PLIK.write("*")
        PLIK.close()

def length(A,B):
    'funkcja wyliczajaca odleglosc puntu A do punktu B, gdzie A,B są w formie [Typ,x,y,z]'
    dl_AB = ((A[1]-B[1])**2+(A[2]-B[2])**2+(A[3]-B[3])**2)**(1/2)
    return(float(dl_AB))
    
        
def czy_jest_wiazanie(elementA,elementB,length):
    'funkcja przyjmujaca jako argumenty Typy A i B oraz długosc pomiedzy nimi, zwracając True or False w zaleznosci czy jest wiazanie'
    bond_length = [['C','H',1.19],['C','O',1.45],['O','H',1.5],['C','C',1.53],['H','H',0.742],['N','H',1.5],['N','O',0.5],['C','N',1.431],['H','F',1.5],['B','H',1.500]]
    for i in range(len(bond_length)):
        if elementA == bond_length[i][0] and elementB == bond_length[i][1] or elementA == bond_length[i][1] and elementB == bond_length[i][0]:
            if bond_length[i][2] >= length:
                return(True)
            else:    
                return(False)
        

def podzial_zbioru_na_dwa(XYZ):
    'funkcja przyjmujaca jako argument AB w formie [Typ,x,y,z] i zwracająca oddzielnie A i B w formie [Typ,x,y,z]'
    G = nx.Graph()
    zwiazane = set()
    for i in range(len(XYZ)):
        for j in range(i+1,len(XYZ)):
            A = XYZ[i][0]
            B = XYZ[j][0]
            dl = length(XYZ[i],XYZ[j])
            if czy_jest_wiazanie(A,B,dl):
                G.add_edge(i,j) 
                zwiazane.add(i)
                zwiazane.add(j) # zapamietujemy indeksy atomow polaczonych wiazaniami
        if not (i in zwiazane):
            G.add_node(i)
    czasteczki = list(nx.connected_components(G))
    TXYZ_A=[XYZ[i] for i in sorted(list(czasteczki[0]))]
    TXYZ_B=[XYZ[i] for i in sorted(list(czasteczki[1]))]
    return TXYZ_A, TXYZ_B


#########################################################################

"Program odczytuje współrzędne poprzez podanie folderu zawierającego dane bądź pliku o formacie .zip"

if not sys.argv[1:]:
    print("Nie podano bazy współrzędnych .xyz")
else:
    source_zip = sys.argv[1]
    if zipfile.is_zipfile(source_zip):
        z = zipfile.ZipFile(source_zip,'r')
        source_zip = PATH.splitext(source_zip)[0]
        with z as coords:
            coords.extractall(str(source_zip))
    for xyz in os.listdir(str(source_zip)+'/'):
        print(xyz)
        TXYZ = TXYZ_tuple(xyz)
        wypisz_do_pliku(TXYZ,xyz)
        TXYZ_AB = podzial_zbioru_na_dwa(TXYZ)
        for i in range(2):
            NAME = xyz.split('.')
            wypisz_do_pliku(TXYZ_AB[i],str(NAME[0]), i) 

#########################################################################






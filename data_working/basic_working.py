'''
Obsługa plików
'''

import time, glob
from Bio import SeqIO
import textwrap
from Bio import Seq
from Bio.SeqRecord import SeqRecord
import os.path



def start(prcr, plstd, dlugoscfragmentu = 500):
    '''
    Funkcja startowa, rozpoznaje co jest jakim rodzajem pliku i dzieli wszystko na dane fragmenty
    :param prcr:
    :param plstd:
    :param dlugoscfragmentu:
    :return:
    '''

    # Potrzbne zmienne

    # Wpierw genomy prokariotów i archeonów
    if prcr[-4:] == '.fna' or prcr[-6:] == '.fasta':
        single_file(prcr, 'prcr', dlugoscfragmentu)
    else:
        whole_folder(prcr, 'prcr', dlugoscfragmentu)

    # Następnie genomy plastydowe

    if plstd[-4:] == '.fna' or plstd[-6:] == '.fasta':
        single_file(plstd, 'plstd', dlugoscfragmentu)
    else:
        whole_folder(plstd, 'plstd', dlugoscfragmentu)



def whole_folder(nazwa, typgenomu, dlugoscfragmentu):
    '''
    Bierze cały folder o strukturze -> Folder : Dużo plików, gdzie każdy odpowiada za pojedynczy gatunek : Każdy plik podzielony na bardzo dużo małych odczytów
    Poszczególe rekordy fasty są dzielone tylko wewnątrz siebie
    Akceptuje tylko pliki o rozszerzeniu fna
    Nazwa gatunku w nazwie pliku
    Odpowiedź w genomy_prcr.fasta -> folder dataset
    :return:
    '''

    outfilename = 'all_' + str((int(time.time()))) + ".fna"
    print("Obróbka prcr")
    with open(os.path.abspath('.') + "/dataset/genomy_" + typgenomu + ".fasta", "w") as output_handle:
        for filename in glob.glob(nazwa + '/*.fna'):
            with open(filename) as handle:
                for record in SeqIO.parse(handle, 'fasta'):
                    fragmenty = []

                    # Uzyskiwanie listy rekordów fragmentów
                    for wrap in textwrap.wrap(str(record.seq), dlugoscfragmentu):
                        if len(wrap) == dlugoscfragmentu:
                            newrecord = SeqRecord(Seq.Seq(wrap), id=record.id)
                            fragmenty.append(newrecord)

                    # Obróbka listy rekordów fragmentów
                    for newrecord in fragmenty:
                        newrecord.id = filename.split("/")[-1]
                        SeqIO.write(newrecord, output_handle, "fasta")


def single_file(nazwa, typgenomu, dlugosc):
    '''
    Wynik znajdzie się w pliku genomy_plstd.fasta w folderze dataset
    Końcówki plików nie zostaną użyte przez program
    :param długosc:
    :return:
    '''
    print("Obróbka plstd")
    filetype = nazwa.split(".")[-1]
    #with open("../dataset/fragmenty_plstd.fasta", 'w') as output_handle:
    with open(os.path.abspath('.') + "/dataset/genomy_" + typgenomu + ".fasta", 'w') as output_handle:
        for record in SeqIO.parse(nazwa, filetype):
            for wrap in textwrap.wrap(str(record.seq), dlugosc):
                if len(wrap) == dlugosc:
                    newrecord = SeqRecord(Seq.Seq(wrap), id=record.id)
                    SeqIO.write(newrecord, output_handle, "fasta")


#single_file('dataset_plstd.fasta', 'plstd', 500)
#whole_folder('TOBGGENOMES', 'prcr', 500)
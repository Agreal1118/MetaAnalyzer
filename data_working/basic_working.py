'''
Obsługa plików
'''

import time, glob
from Bio import SeqIO
import textwrap
from Bio import Seq
from Bio.SeqRecord import SeqRecord



def start(prcr, plstd, dlugoscfragmentu = 500):
    '''
    Funkcja startowa, rozpoznaje co jest jakim rodzajem pliku i dzieli wszystko na dane fragmenty
    :param prcr:
    :param plstd:
    :param dlugoscfragmentu:
    :return:
    '''

    # Wpierw genomy prokariotów i archeonów
    if prcr[:4] == '.fna' or prcr[:6] == '.fasta':
        single_file(prcr)
    else:
        whole_folder(prcr, 'prcr', dlugoscfragmentu)

    # Następnie genomy plastydowe
    if plstd[:4] == '.fna' or plstd[:6] == '.fasta':
        single_file(plstd)
    else:
        whole_folder(plstd, 'plstd', dlugoscfragmentu)



def whole_folder(nazwa, typgenomu, dlugoscfragmentu):
    '''
    Bierze cały folder o strukturze -> Folder : Dużo plików, gdzie każdy odpowiada za pojedynczy gatunek : Każdy plik podzielony na bardzo dużo małych odczytów
    Poszczególe rekordy fasty są dzielone tylko wewnątrz siebie
    Akceptuje tylko pliki o rozszerzeniu fna
    Nazwa gatunku w nazwie pliku
    Odpowiedź w fragmenty_prcr.fasta -> folder dataset
    :return:
    '''

    outfilename = 'all_' + str((int(time.time()))) + ".fna"

    with open("../dataset/fragmenty_" + typgenomu + ".fasta", "w") as output_handle:
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
    Wynik znajdzie się w pliku fragmenty_plstd.fasta w folderze dataset
    Końcówki plików nie zostaną użyte przez program
    :param długosc:
    :return:
    '''
    filetype = nazwa.split(".")[-1]
    #with open("../dataset/fragmenty_plstd.fasta", 'w') as output_handle:
    with open("../dataset/fragmenty_" + typgenomu + ".fasta", 'w') as output_handle:
        for record in SeqIO.parse(nazwa, filetype):
            for wrap in textwrap.wrap(str(record.seq), dlugosc):
                if len(wrap) == dlugosc:
                    newrecord = SeqRecord(Seq.Seq(wrap), id=record.id)
                    SeqIO.write(newrecord, output_handle, "fasta")


#single_file('dataset_plstd.fasta', 'plstd', 500)
#whole_folder('TOBGGENOMES', 'prcr', 500)
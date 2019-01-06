from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import random
import os

listaDlugosci = (500, 1000, 1500) # krotka trzymająca docelowe możliwe długości argumentów

nazwa = "plastids_db.fa"

#wynik znajdzie się w pliku fragmenty.fasta
with open("fragmenty.fasta", "w") as output_handle:
    # wczytywanie genomów plastydowych
    for record in SeqIO.parse(nazwa, "fasta"):
        x = len(record.seq)
        leng = 0
        while x > 500:
            rand = random.choice(listaDlugosci)
            if rand <= x:
                x -= rand
                leng += rand
                # tworzenie nowego rekordu typu fasta, najpierw tworzy sekwencję typu Seq złożoną z sekwencji i z rodzaju informacji w niej zawartej
                # potem z seq oraz id i opisu tworzy rekord
                newrecord = SeqRecord(Seq.Seq(str(record.seq[(leng-rand):leng]), IUPAC.unambiguous_dna), id=record.id + " " + str(leng-rand) + " - " + str(leng), description=record.description)
                SeqIO.write(newrecord, output_handle, "fasta")
    # wczytywanie genomów prokariotycznych
    for filename in os.listdir(os.getcwd()+"/TOBGGENOMES"):
        for record in SeqIO.parse(os.getcwd()+"/TOBGGENOMES/"+filename, "fasta"):
            x = len(record.seq)
            leng = 0
            while x > 500:
                rand = random.choice(listaDlugosci)
                if rand <= x:
                    x -= rand
                    leng += rand
                    newrecord = SeqRecord(Seq.Seq(str(record.seq[(leng - rand):leng]), IUPAC.unambiguous_dna),
                                          id=record.id + " " + str(leng - rand) + " - " + str(leng),
                                          description=record.description)
                    SeqIO.write(newrecord, output_handle, "fasta")
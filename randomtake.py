'''
Do danych podglądowych
Zadaniem pliku jest wzięcie losowej próbki z obu plików genomów 
plastydowych i prokariotycznych, o rozmiarze 500 ustalanym w linii 17.
'''

from Bio import SeqIO
import random
def hundred():
    seqprcr = []
    seqplstd = []
    for record in SeqIO.parse('dane/fragmenty_prcr.fasta', 'fasta'):
        seqprcr.append(record.seq)
    for record in SeqIO.parse('dane/fragmenty_plstd.fasta', 'fasta'):
        seqplstd.append(record.seq)

    seq = random.sample(seqplstd, 500) + random.sample(seqprcr,  500)



    return seq
    #for record in SeqIO.parse('dane/fragmenty_prcr.fasta', "fasta"):
    #    pass


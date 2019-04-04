from Bio import SeqIO
import random

'''

Plik służący do losowania elementów danych - do danych próbnych

'''

def randomFromFragments(ilewylosowac, czydopliku=False):
    '''
    Losowanie danej ilości fragmentów ze stworzonej bazy fragmentów dna plastydowych i prokariotycznych
    Dane zwracane w liście ----> [seqprcr, seqplst, ....]
    '''
    seqprcr = []
    seqplstd = []
    for record in SeqIO.parse('../dataset/fragmenty_prcr.fasta', 'fasta'):
        seqprcr.append(record)
    for record in SeqIO.parse('../dataset/fragmenty_plstd.fasta', 'fasta'):
        seqplstd.append(record)
    sampleplstd = random.sample(seqplstd, ilewylosowac)
    sampleprcr = random.sample(seqprcr,  ilewylosowac)

    if czydopliku == False:
        return (sampleprcr, sampleplstd)
    else:
        SeqIO.write(sampleplstd, '../dataset/sample_plstd.fasta', 'fasta')
        SeqIO.write(sampleprcr, '../dataset/sample_prcr.fasta', 'fasta')



def randomFromDataset(ilewylosowacplstd, ilewylosowacprcr, czydopliku=False):
    '''
    Losowanie danej ilości genomów/fragmentów metagenomowych z dużego datasetu
    Możliwy zapis do pliku, dla stabilizacji testu
    W innym wypadku zwraca listę z dwoma records z SeqIO.parse --> odwołania z record.seq i record.
    :param ilewylosowac:
    :param czydopliku:
    :return:
    '''

    seqprcr = []
    seqplstd = []
    #bit = []
    #lastid = ""
    for record in SeqIO.parse('../dataset/dataset_prcr.fasta', 'fasta'):
        '''
        if record.id != lastid:
            if bit != []:
                seqprcr.append(bit)
            bit = []
            lastid == record.id
            bit.append(record)
        else:
        '''
        seqprcr.append(record)
    for record in SeqIO.parse('../dataset/dataset_plstd.fasta', 'fasta'):
        seqplstd.append(record)
    recordsplstd = random.sample(seqplstd, ilewylosowacplstd)
    recordsprcr = random.sample(seqprcr, ilewylosowacprcr)

    if czydopliku == False:
        return [recordsplstd, recordsprcr]
    else:
        SeqIO.write(recordsplstd, '../dataset/partofdataset_plstd.fasta', 'fasta')
        SeqIO.write(recordsprcr, '../dataset/partofdataset_prcr.fasta', 'fasta')


randomFromFragments(500, True)
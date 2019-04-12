import representation.dnavec as dnavec
from Bio import SeqIO
from gensim.models import word2vec
import visualization.visualization as visualization
import numpy as np
import classification.randomForest as rf
import classification.svm as svm
import time

#model = dnavec.generate_corpusfile(['dataset/sample_plstd.fasta', 'dataset/sample_prcr.fasta'], 3, 'dataset/dnaVecCorpus.txt')
# generate corpusse file działą

dnavecs = []
print ("Chcesz stworzyć nowy korpus, wczytać korpus, czy wczytać model (zalecane)? (nowy/korpus/model/gotowy)")
z = input()

if (z=='nowy'):
    model = dnavec.DnaVec(['dataset/sample_plstd.fasta', 'dataset/sample_prcr.fasta'])
    model.save('dataset/dnavec/dnavec.model')
    # generowanie modelu działa
    dnavecs = []
    for record in SeqIO.parse("dataset/genomy_plstd.fasta", 'fasta'):
        vec = model.to_vecs(record)
        vec = vec[0] + vec[1] + vec[2]
        print(type(vec))
        vec = [vec, 'plstd']
        dnavecs.append(vec)
    for record in SeqIO.parse("dataset/genomy_prcr.fasta", 'fasta'):
        vec = model.to_vecs(record)
        vec = vec[0] + vec[1] + vec[2]
        # print(vec)
        vec = [vec, 'prcr']
        dnavecs.append(vec)
        np.save("dataset/dnavec/nmp.npy", dnavecs)

elif (z=='korpus'):
    model = dnavec.DnaVec(corpus=True)
    model.save('dataset/dnavec/dnavec.model')
    # generowanie modelu działa
    dnavecs = []
    for record in SeqIO.parse("dataset/genomy_plstd.fasta", 'fasta'):
        vec = model.to_vecs(record)
        vec = vec[0] + vec[1] + vec[2]
        print(type(vec))
        vec = [vec, 'plstd']
        dnavecs.append(vec)
    for record in SeqIO.parse("dataset/genomy_prcr.fasta", 'fasta'):
        vec = model.to_vecs(record)
        vec = vec[0] + vec[1] + vec[2]
        # print(vec)
        vec = [vec, 'prcr']
        dnavecs.append(vec)
        np.save("dataset/dnavec/nmp.npy", dnavecs)

elif (z=='model'):
    model = word2vec.Word2Vec.load('dataset/dnavec/dnavec.model')
    # generowanie modelu działa
    dnavecs = []
    for record in SeqIO.parse("dataset/genomy_plstd.fasta", 'fasta'):
        vec = model.to_vecs(record)
        vec = vec[0] + vec[1] + vec[2]
        vec = [vec, 'plstd']
        dnavecs.append(vec)
    for record in SeqIO.parse("dataset/genomy_prcr.fasta", 'fasta'):
        vec = model.to_vecs(record)
        vec = vec[0] + vec[1] + vec[2]
        # print(vec)
        vec = [vec, 'prcr']
        dnavecs.append(vec)
    np.save("dataset/dnavec/nmp.npy", dnavecs)
elif (z=="gotowy"):
    czas = time.time()

    dnavecs = np.load("dataset/dnavec/nmp.npy")

    print("wczytanie " + str(time.time()-czas))



print ("Klasyfikacja? (svm/rf)")
z = input()
if z=='svm':
    svm.svm(dnavecs)

if z=='rf':
    rf.randomforest(dnavecs)

print("wizualizajca? (T/N)")
z = input()
if z=='T':
    visualization.pca(dnavecs)
    visualization.tsnesolo(dnavecs)
    visualization.tsnePcaReduction(dnavecs)
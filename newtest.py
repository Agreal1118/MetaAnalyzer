import representation.dnavec as dnavec
from Bio import SeqIO
import visualization.visualization as visualization

import classification.svm as svm

#model = dnavec.generate_corpusfile(['dataset/sample_plstd.fasta', 'dataset/sample_prcr.fasta'], 3, 'dataset/dnaVecCorpus.txt')
# generate corpusse file działą

dnavecs = []
print ('Tworzyć nowy korpus? (T/N)')
z = input()
if (z=='T'):
    model = dnavec.DnaVec(['dataset/sample_plstd.fasta', 'dataset/sample_prcr.fasta'])
elif (z=='N'):
    model = dnavec.DnaVec(corpus=True)


# generowanie modelu działa
dnavecs = []
for record in SeqIO.parse("dataset/sample_plstd.fasta", 'fasta'):
    vec = model.to_vecs(record)
    vec = vec[0] + vec[1] + vec[2]
    #print (vec)
    vec = [vec, 'plstd']
    dnavecs.append(vec)
for record in SeqIO.parse("dataset/sample_prcr.fasta", 'fasta'):
    vec = model.to_vecs(record)
    vec = vec[0] + vec[1] + vec[2]
    #print(vec)
    vec = [vec, 'prcr']
    dnavecs.append(vec)

#visualization.pca(dnavecs)
#visualization.tsnesolo(dnavecs)
#visualization.tsnePcaReduction(dnavecs)


svm.svm(dnavecs)
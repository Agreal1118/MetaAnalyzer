from gensim.models import word2vec
import sys
from gensim.models import word2vec
from tqdm import tqdm
from Bio import SeqIO
from pyfasta import Fasta


def binary_nucleo():
    '''
    Binary representation of amino acid residue and amino acid sequence
    e.g.
        'A' => [0, 0, 0, 0, 0]
        'AGGP' => [[0, 0, 0, 0, 0], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 1, 1]]
    '''
    NUCLEOTIDE_BINARY_TABLE = {
        'A': [0, 0],
        'C': [0, 1],
        'G': [1, 0],
        'T': [1, 1],
    }

    def convert_nucleotide_to_binary(nucleotide):
        '''
        Convert amino acid to 1-dimentional 5 length binary array
        "A" => [0, 0, 0, 0, 0]
        '''
        if not NUCLEOTIDE_BINARY_TABLE.has_key(nucleotide):
            return None
        return NUCLEOTIDE_BINARY_TABLE[nucleotide]

    def convert_nucleotide_sequence_to_vector(sequence):
        '''
        "AGGP" => [[0, 0, 0, 0, 0], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 1, 1]]
        '''
        binary_vector = [convert_nucleotide_to_binary(nucleotide) for nucleotide in sequence]
        if None in binary_vector:
            return None
        return binary_vector


def split_ngrams(seq, n):
    """
    'ACATGC' => [['ACA', 'TGC'], ['CAT'], ['ATG']]
    """
    a, b, c = zip(*[iter(seq)]*n), zip(*[iter(seq[1:])]*n), zip(*[iter(seq[2:])]*n)
    str_ngrams = []
    for ngrams in [a,b,c]:
        x = []
        for ngram in ngrams:
            x.append("".join(ngram))
        str_ngrams.append(x)
    return str_ngrams


def generate_corpusfile(fasta_fname, n, corpus_fname):
    '''
    Args:
        fasta_fname: corpus file name
        n: the number of chunks to split. In other words, "n" for "n-gram"
        corpus_fname: corpus_fnameput corpus file path
    Description:
        Protvec uses word2vec inside, and it requires to load corpus file
        to generate corpus.
    '''

    f = open(corpus_fname, "w")

    for record in tqdm(SeqIO.parse(fasta_fname, "fasta"), desc='corpus generation progress'):
        ngram_patterns = split_ngrams(record.seq, n)
        for ngram_pattern in ngram_patterns:
            f.write(" ".join(ngram_pattern) + "\n")
    f.close()



def load_dnavec(model_fname):
    return word2vec.Word2Vec.load(model_fname)


class DnaVec(word2vec.Word2Vec):

    def __init__(self, fasta_fname=None, corpus=None, n=3, size=100, corpus_fname="corpus.txt",  sg=1, window=25, min_count=1, workers=3):
        """
        Either fname or corpus is required.

        fasta_fname: fasta file for corpus
        corpus: corpus object implemented by gensim
        n: n of n-gram
        corpus_fname: corpus file path
        min_count: least appearance count in corpus. if the n-gram appear k times which is below min_count, the model does not remember the n-gram
        """

        self.n = n
        self.size = size
        self.fasta_fname = fasta_fname

        if corpus is None and fasta_fname is None:
            raise Exception("Either fasta_fname or corpus is needed!")

        if fasta_fname is not None:
            print('Generate Corpus file from fasta file...')
            generate_corpusfile(fasta_fname, n, corpus_fname)
            corpus = word2vec.Text8Corpus(corpus_fname)

        word2vec.Word2Vec.__init__(self, corpus, size=size, sg=sg, window=window, min_count=min_count, workers=workers)

    def to_vecs(self, seq):
        """
        convert sequence to three n-length vectors
        e.g. 'AGAMQSASM' => [ array([  ... * 100 ], array([  ... * 100 ], array([  ... * 100 ] ]
        """
        ngram_patterns = split_ngrams(seq, self.n)

        dnavecs = []
        for ngrams in ngram_patterns:
            ngram_vecs = []
            for ngram in ngrams:
                try:
                    ngram_vecs.append(self[ngram])
                except:
                    raise Exception("Model has never trained this n-gram: " + ngram)
            dnavecs.append(sum(ngram_vecs))
        return dnavecs

x = DnaVec('fragmenty.fasta')
print(len(x.to_vecs('ATTGTTTTGATATGCTTCATAAGAATTTTCT')[0]))
print(x.to_vecs('ATTGTTTTGATATGCTTCATAAGAATTTTCT'))
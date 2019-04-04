import representation.dnavec as dnavec
import visualization.visualization as visualization
import representation.randomtake as randomtake
import pickle
import system
import getopt

def stary():
    #print('Podaj metodę wyświetlenia (tsne, tsne-pca, pca, all)')
    wysw = 'all'

    #if inpt == 'dnavec':

    if wysw == 'all':
        dnavecs = []
        print ('Tworzyć nowy korpus? (T/N)')
        z = input()
        if (z=='T'):
            print ('Uwaga generacja noweg korpusu jest bardzo czasochłonna, potwierdź swój wybór [nowykorpus[')
            z = input()
            if z == 'nowykorpus':
                model = dnavec.DnaVec('dane/fragmenty_wszystkie.fasta')
        elif (z=='N'):
            model = dnavec.DnaVec(corpus=True)

        print('Chcesz generować nową próbkę fragmentów genomów? (T/N)')
        z = input()
        if (z=='T'):
            licz = 0
            for record in randomtake.hundred():
                licz += 1
                vec = model.to_vecs(record)
                vec = vec[0] + vec[1] + vec[2]
                # print ('oto to')
                # print (vec)
                if licz > 500:
                    vec = [vec, 'plstd']
                else:
                    vec = [vec, 'prcr']
                # print('oto to')
                # print(vec)
                dnavecs.append(vec)

            infile = open("dane/sample.txt", "wb")
            pickle.dump(dnavecs, infile)
            infile.close()
            #print(dnavecs)
        elif (z=='N'):
            infile = open("dane/sample.txt", "rb")
            dnavecs = pickle.load(infile)
            infile.close()
            #with open("dane/sample.txt", "rb") as input:
            #    for i in input:
            #        dnavecs.append(pickle.load(input))
            #print(dnavecs)

        visualization.pca(dnavecs)
        visualization.tsnesolo(dnavecs)
        visualization.tsnePcaReduction(dnavecs)

###################################################################################
# obsługa parametrów i modułów

'''
def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])

'''
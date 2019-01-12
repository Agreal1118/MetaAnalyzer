import dnavec
import visualization
import randomtake
import pickle


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

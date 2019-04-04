import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE


def pca(sequances):
    '''

    Funkcja bierze dwuwymiarową listę wektorów [sekwencja, pochodzenie] i wyświetlna ją w atrakcyjnej formie
    '''

    #tworzymy macierz danych akceptowaną przez pandas
    labels = pd.DataFrame.from_records(sequances)
    x = pd.DataFrame.from_records(labels[0])
    y = labels[1]
    #print (x[0])
    #print(x)

    #teraz konieczne jest przeprowadzenie standaryzacji danych do formy średnia=0 i wariancja=1
    standardlabels = StandardScaler().fit_transform(x)
    #print(standardlabels)
    #standardlabels = x
    #teraz sprowadzamy liczbę wymiarów do 2
    pca = PCA(n_components=2)

    mainComponent = pca.fit_transform(standardlabels)
    mainDf = pd.DataFrame(data=mainComponent)
    #print(mainDf)

    #mówi o tym ile informacji trzyma każdy z komponentów, nie sumuje się do 100
    #print(pca.explained_variance_ratio_)

    #czas na wizualizację otrzymanej macierzy
    #mainDf.plot.scatter(x='Komponent 1', y='Komponent 2')
    final = pd.concat([mainDf, y], axis=1)
    final.columns = ['Komponent 1', 'Komponent 2', 'Pochodzenie']
    #print (final)
    #plt.show()
    #plt.savefig('myplota.png')

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Komponent 1', fontsize=15)
    ax.set_ylabel('Komponent 2', fontsize=15)
    ax.set_title('PCA', fontsize=25)

    targets = ['plstd', 'prcr']
    colors = ['r', 'b']

    #print (list(final))

    for target, color in zip(targets, colors):

        ax.scatter(final.loc[final['Pochodzenie'] == target, 'Komponent 1']
                   ,final.loc[final['Pochodzenie'] == target, 'Komponent 2']
                   ,c=color)

    ax.legend(targets)
    ax.grid()
    #plt.show()
    plt.savefig('result/pca.png')


def tsnesolo(sequances):

    labels = pd.DataFrame.from_records(sequances)
    x = pd.DataFrame.from_records(labels[0])
    y = labels[1]

    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    tsne_results = tsne.fit_transform(x)
    tsne_results = pd.DataFrame.from_records(tsne_results)
    #print (tsne_results)

    tsnefinal = pd.concat([tsne_results, y], axis=1)
    tsnefinal.columns = ['Komponent 1', 'Komponent 2', 'Pochodzenie']

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Komponent 1', fontsize=15)
    ax.set_ylabel('Komponent 2', fontsize=15)
    ax.set_title('TSNE', fontsize=25)

    targets = ['plstd', 'prcr']
    colors = ['r', 'b']

    #print(list(tsnefinal))

    for target, color in zip(targets, colors):
        ax.scatter(tsnefinal.loc[tsnefinal['Pochodzenie'] == target, 'Komponent 1']
                   , tsnefinal.loc[tsnefinal['Pochodzenie'] == target, 'Komponent 2']
                   , c=color)

    ax.legend(targets)
    ax.grid()
    # plt.show()
    plt.savefig('result/tsnesolo.png')


def tsnePcaReduction(sequances):



    labels = pd.DataFrame.from_records(sequances)
    x = pd.DataFrame.from_records(labels[0])
    y = labels[1]

    pca_50 = PCA(n_components=50)
    pca_result_50 = pca_50.fit_transform(x[list(x)].values)

    #print(x)
    #print ('boziu w niebiosach')
    #print(pca_result_50)

    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    tsne_results = tsne.fit_transform(pca_result_50)
    tsne_results = pd.DataFrame.from_records(tsne_results)
    #print(tsne_results)

    tsnefinal = pd.concat([tsne_results, y], axis=1)
    tsnefinal.columns = ['Komponent 1', 'Komponent 2', 'Pochodzenie']

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Komponent 1', fontsize=15)
    ax.set_ylabel('Komponent 2', fontsize=15)
    ax.set_title('TSNE-PCA', fontsize=25)

    targets = ['plstd', 'prcr']
    colors = ['r', 'b']

    #print(list(tsnefinal))

    for target, color in zip(targets, colors):
        ax.scatter(tsnefinal.loc[tsnefinal['Pochodzenie'] == target, 'Komponent 1']
                   , tsnefinal.loc[tsnefinal['Pochodzenie'] == target, 'Komponent 2']
                   , c=color)

    ax.legend(targets)
    ax.grid()
    # plt.show()
    plt.savefig('result/tsnepca.png')
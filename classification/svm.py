from sklearn import svm


def svm():

    # tworzenie modelu o odpowiednich paramterach
    clf = svm.SVC(gamma='scale')

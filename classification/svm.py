from sklearn import svm as sv
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
from sklearn.svm import SVC
import gc


def svm(sequances):

    # tworzenie modelu o odpowiednich paramterach

    clf = sv.SVC(gamma='scale')
    print("Model SVC wczytany")

    labels = pd.DataFrame.from_records(sequances)
    print ("z sekwencji stworzono pd dataframe")
    x = pd.DataFrame.from_records(labels[0])
    '''
    Wygląd x
                    0          1          2   ...         97         98          99
        0     4.991699   5.341255 -32.386837  ...  22.653732 -12.949523 -109.862022
        1    13.883627  20.495790 -30.535908  ...  40.336170  -1.560726 -117.623039
        '''
    y = labels[1]
    '''
    Wygląd y
        0      plstd
        1      plstd
    '''

    labels=None
    gc.collect()

    #standardlabels = StandardScaler().fit_transform(x)


# Redukcja wymiarowa
    pca = PCA(n_components=2)
    mainComponent = pca.fit_transform(x)
    mainDf = pd.DataFrame(data=mainComponent)

    print("redukcja wymiaru skończona")

    x = None
    gc.collect()

    X_train, X_test, y_train, y_test = train_test_split(mainDf, y, test_size = 0.33, random_state = 42)

    clf.fit(X_train, y_train)
    print("fit modelu skończon")

    ypred=clf.predict(X_test)
    print("predykcja skończona")

    print ("wynik predykcji to " + str(clf.score(X_test, y_test)))
    print(classification_report(y_test, ypred))
    print(confusion_matrix(y_test, ypred))

    print ('\n\n\n\n\###########################################################')

    np.random.seed(123)
    g_range = np.random.uniform(0.0, 0.3, 5).astype(float)
    C_range = np.random.normal(1, 0.1, 5).astype(float)

    C_range[C_range < 0] = 0.0001

    hyperparameters = {'gamma': list(g_range),
                       'C': list(C_range)}

    print(hyperparameters)

    #######################

    randomCV = RandomizedSearchCV(SVC(kernel='rbf', ), param_distributions=hyperparameters, n_iter=20)
    randomCV.fit(X_train, y_train)

    # Identify optimal hyperparameter values
    best_gamma = randomCV.best_params_['gamma']
    best_C = randomCV.best_params_['C']

    print("The best performing gamma value is: {:5.2f}".format(best_gamma))
    print("The best performing C value is: {:5.2f}".format(best_C))

    # Train SVM and output predictions
    rbfSVM = SVC(kernel='rbf', C=best_C, gamma=best_gamma)
    rbfSVM.fit(X_train, y_train)
    svm_predictions = rbfSVM.predict(X_test)

    print(classification_report(y_test, svm_predictions))
    print("Overall Accuracy:", str(rbfSVM.score(X_test, y_test)))
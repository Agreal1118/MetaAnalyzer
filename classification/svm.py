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


def svm(labels):

    # tworzenie modelu o odpowiednich paramterach

    clf = sv.SVC(gamma='scale')
    print("Model SVC wczytany")

    '''
    wygląd labels
                                                   0      1
    0        [-8.213443603919687, 3.915492349439239]  plstd
    1       [4.103066531114637, 0.19115485017195025]  plstd
    2    [-3.6886699085529813, -0.38134145597406094]  plstd
    '''

    x = pd.DataFrame.from_records(labels[0])
    y = labels[1]

    labels=None
    gc.collect()

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)

    x = None
    gc.collect()

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
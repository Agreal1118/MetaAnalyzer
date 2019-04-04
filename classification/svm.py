from sklearn import svm as sv
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



def svm(sequances):

    # tworzenie modelu o odpowiednich paramterach
    clf = sv.SVC(gamma='scale')


    labels = pd.DataFrame.from_records(sequances)
    x = pd.DataFrame.from_records(labels[0])
    y = labels[1]

    #standardlabels = StandardScaler().fit_transform(x)


# Redukcja wymiarowa
    pca = PCA(n_components=2)
    mainComponent = pca.fit_transform(x)
    mainDf = pd.DataFrame(data=mainComponent)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)

    clf.fit(X_train, y_train)

    ypred=clf.predict(X_test)

    print(classification_report(y_test, ypred))
    print(confusion_matrix(y_test, ypred))

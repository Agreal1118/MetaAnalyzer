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
from sklearn.ensemble import RandomForestClassifier
import gc


def randomforest(labels):

    x = pd.DataFrame.from_records(labels[0])
    y = labels[1]

    labels = None #czyszczenie pamięci
    gc.collect()



    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)



    # Designate distributions to sample hyperparameters from
    n_estimators = np.random.uniform(70, 80, 5).astype(int)
    max_features = np.random.normal(6, 3, 5).astype(int)

    # Check max_features>0 & max_features<=total number of features
    max_features[max_features <= 0] = 1
    max_features[max_features > x.shape[1]] = x.shape[1]

    x = None
    gc.collect()

    hyperparameters = {'n_estimators': list(n_estimators),
                       'max_features': list(max_features)}

    print(hyperparameters)

    # Run randomized search
    randomCV = RandomizedSearchCV(RandomForestClassifier(), param_distributions=hyperparameters, n_iter=20, n_jobs=20)
    randomCV.fit(X_train, y_train)

    # Identify optimal hyperparameter values
    best_n_estim = randomCV.best_params_['n_estimators']
    best_max_features = randomCV.best_params_['max_features']

    print("The best performing n_estimators value is: {:5d}".format(best_n_estim))
    print("The best performing max_features value is: {:5d}".format(best_max_features))

    # Train classifier using optimal hyperparameter values
    # We could have also gotten this model out from randomCV.best_estimator_
    rf = RandomForestClassifier(n_estimators=best_n_estim,
                                max_features=best_max_features,
                                class_weight='balanced',
                                n_jobs=20
                                )

    rf.fit(X_train, y_train)
    rf_predictions = rf.predict(X_test)

    print(classification_report(y_test, rf_predictions))
    print("Overall Accuracy:", str(rf.score(X_test, y_test)))


    ##################################
    ### Tutaj bez random search
    ##################################

    # Create default rf
    rf = RandomForestClassifier()
    print(rf.get_params)

    # Fit and predict with default rf
    rf.fit(X_train, y_train)
    rf_predictions = rf.predict(X_test)

    print(classification_report(y_test, rf_predictions))
    print("Overall Accuracy:", str(rf.score(X_test, y_test)))

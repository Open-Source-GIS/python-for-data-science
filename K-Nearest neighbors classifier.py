from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# A simple example shipped with the scikit: iris dataset
# 150 observations of irises, each described by 4 features: 
# their sepal and petal length and width# Split iris data in train and test data
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# sorted array target values 
np.unique(iris_y)

# simplest possible classifier is the nearest neighbor
# given a new observation X_test, find in the training set (i.e. the data used 
# to train the estimator) the observation with the closest feature vector. 


# When experimenting with learning algorithm, it is important not to test the prediction 
# of an estimator on the data used to fit the estimator, as this would not be evaluating 
# the performance of the estimator on new data.

# Split iris data in train and test data
# A random permutation, to split the data randomly by shuffling array elements
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test  = iris_y[indices[-10:]]

# Create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()

# All supervised estimators in the scikit-learn implement a fit(X, y) method 
# to fit the model, and a predict(X) method that, given unlabeled observations X, 
# returns the predicted labels y
knn.fit(iris_X_train, iris_y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, n_neighbors=5, p=2,
           warn_on_equidistant=True, weights='uniform')
knn.predict(iris_X_test)

# For an estimator to be effective, you need the distance between neighboring points 
# to be less than some value d, which depends on the problem. In one dimension, 
# this requires on average n ~ 1/d points. So 1/n for this example.
print iris_y_test

# If the number of features is p, you now require n ~ 1/d^p points. 
# Let’s say that we require 10 points in one dimension: Now 10^p points are required 
# in p dimensions to pave the [0, 1] space. As p becomes large, the number of training 
# points required for a good estimator grows exponentially (curse of dimensionality).


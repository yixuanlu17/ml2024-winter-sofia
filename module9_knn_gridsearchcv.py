import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score

def read_pairs(n):
    """Reads n pairs of (x, y) from the user and returns them as numpy arrays."""
    x_vals = []
    y_vals = []
    for _ in range(n):
        x = float(input("Enter x value: "))
        y = int(input("Enter y value: "))
        x_vals.append(x)
        y_vals.append(y)
    return np.array(x_vals).reshape(-1, 1), np.array(y_vals)

# Main program
N = int(input("Enter N (number of training pairs): "))
train_X, train_y = read_pairs(N)

M = int(input("Enter M (number of test pairs): "))
test_X, test_y = read_pairs(M)

# Setting up the parameter grid for k values from 1 to 10
param_grid = {'n_neighbors': list(range(1, 11))}

# Creating the kNN classifier and GridSearchCV objects
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')

# Fitting GridSearchCV on the training data
grid_search.fit(train_X, train_y)

# Predicting on the test set with the best found model
best_knn = grid_search.best_estimator_
predictions = best_knn.predict(test_X)

# Calculating and printing the best k and test accuracy
best_k = grid_search.best_params_['n_neighbors']
test_accuracy = accuracy_score(test_y, predictions)
print(f"The best k is {best_k} with a test accuracy of {test_accuracy}.")

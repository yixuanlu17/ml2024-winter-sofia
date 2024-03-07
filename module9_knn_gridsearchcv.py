
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
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

def find_best_k(train_X, train_y, test_X, test_y):
    """Finds the best k for kNN classifier based on test set accuracy."""
    best_accuracy = 0
    best_k = 1
    for k in range(1, 11):  # Trying k from 1 to 10
        classifier = KNeighborsClassifier(n_neighbors=k)
        classifier.fit(train_X, train_y)
        predictions = classifier.predict(test_X)
        accuracy = accuracy_score(test_y, predictions)
        print(f"k={k}, Test Accuracy={accuracy}")
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    return best_k, best_accuracy

# Main program
N = int(input("Enter N (number of training pairs): "))
train_X, train_y = read_pairs(N)

M = int(input("Enter M (number of test pairs): "))
test_X, test_y = read_pairs(M)

best_k, best_accuracy = find_best_k(train_X, train_y, test_X, test_y)
print(f"The best k is {best_k} with a test accuracy of {best_accuracy}.")

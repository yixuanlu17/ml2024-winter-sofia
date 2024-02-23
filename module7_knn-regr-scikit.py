import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def main():
    # Read N
    N = int(input("Enter the number of points N (positive integer): "))
    
    # Read k
    k = int(input("Enter the number of nearest neighbors k (positive integer): "))
    
    # Check if k <= N
    if k > N:
        print("Error: k cannot be greater than N.")
        return
    
    # Initialize arrays for storing points
    points = np.zeros((N, 2))
    
    # Read N (x, y) points
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        points[i] = [x, y]
    
    # Split points into features (X) and target (Y)
    X = points[:, 0].reshape(-1, 1) # Reshape for sklearn compatibility
    Y = points[:, 1]
    
    # Ask for input X to predict Y
    X_pred = float(input("Enter X value to predict Y: "))
    X_pred = np.array([[X_pred]]) # Reshape and wrap in 2D array for prediction
    
    # Perform k-NN Regression
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, Y)
    Y_pred = knn.predict(X_pred)
    
    print(f"The predicted Y value is: {Y_pred[0]}")
    
    # Calculate and print the coefficient of determination R^2
    Y_all_pred = knn.predict(X)
    r2 = r2_score(Y, Y_all_pred)
    print(f"Coefficient of determination (R^2): {r2}")

if __name__ == "__main__":
    main()

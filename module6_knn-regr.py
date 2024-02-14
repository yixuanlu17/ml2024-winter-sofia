
import numpy as np

def read_points(N):
    points = np.empty((N, 2))
    for i in range(N):
        x, y = map(float, input(f"Enter x and y for point {i+1} (separated by space): ").split())
        points[i] = [x, y]
    return points

def k_nn_regression(points, k, X):
    distances = np.sqrt((points[:, 0] - X) ** 2)
    nearest_indices = np.argsort(distances)[:k]
    nearest_y_values = points[nearest_indices, 1]
    return np.mean(nearest_y_values)

def main():
    N = int(input("Enter N (positive integer): "))
    k = int(input("Enter k (positive integer): "))
    
    if k > N:
        print("Error: k cannot be greater than N.")
        return
    
    print("Now enter N (x, y) points one by one.")
    points = read_points(N)
    
    X = float(input("Enter X (the x value for prediction): "))
    result_Y = k_nn_regression(points, k, X)
    
    print(f"The result (Y) of {k}-NN Regression is: {result_Y}")

if __name__ == "__main__":
    main()

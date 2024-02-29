
import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask for the number of points
    N = int(input("Enter the number of points N: "))
    
    # Initialize arrays for ground truth and predicted values
    ground_truth = np.zeros(N, dtype=int)
    predicted = np.zeros(N, dtype=int)
    
    # Read N points
    for i in range(N):
        x = int(input(f"Enter x (0 or 1) value for point {i+1}: "))
        y = int(input(f"Enter y (0 or 1) value for point {i+1}: "))
        ground_truth[i] = x
        predicted[i] = y
    
    # Compute Precision and Recall
    precision = precision_score(ground_truth, predicted)
    recall = recall_score(ground_truth, predicted)
    
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    main()

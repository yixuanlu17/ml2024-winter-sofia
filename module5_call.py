
from module5_mod import NumberStorage

def main():
    storage = NumberStorage()
    
    N = int(input("Enter the number of elements N: "))
    
    for i in range(N):
        number = int(input(f"Enter number {i+1}: "))
        storage.insert(number)
    
    X = int(input("Enter the number X to search for: "))
    result = storage.search(X)
    
    if result == -1:
        print("-1 (No such number found)")
    else:
        print(f"The number {X} was found at position: {result}")

if __name__ == "__main__":
    main()

def simple_program():
    # Asking the user for the number of inputs (N)
    N = int(input("Enter the number of elements (N): "))

    # Initializing an empty list to store the numbers
    numbers = []

    # Reading N numbers from the user
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Asking the user for the target number (X)
    X = int(input("Enter the number to find (X): "))

    # Checking if X is in the list and finding its index
    if X in numbers:
        index = numbers.index(X) + 1  # Adding 1 to make it 1-indexed
        print(index)
    else:
        print("-1")

# Running the program
simple_program()

def Bubble_Sort(arr):
    # If the array has only one element or is empty, return it as it is already sorted
    if len(arr) <= 1:
        return arr

    else:
        # Iterate through the array
        for i in range(len(arr)):
            # Initialize a flag to track if any swaps were made in this iteration
            swapped = False
            # Iterate through the array, comparing each element with its adjacent element
            for j in range(len(arr) - i - 1):
                # If the current element is greater than the next element, swap them
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    # Set the flag to True, indicating that a swap was made
                    swapped = True
            # If no swaps were made in this iteration, the array is already sorted
            # We can break out of the loop early, as no further swaps are needed
            if not swapped:
                break
        # Return the sorted array
        return arr

arr = [3, 6, -9, 1, -45, 8, 5]
result = Bubble_Sort(arr)
print(result)  # [-45, -9, 1, 3, 5, 6, 8]
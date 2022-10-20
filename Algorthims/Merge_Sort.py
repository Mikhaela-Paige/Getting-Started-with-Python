"""
Merge sort is an algorithm that follows the Divide-and-Conquer strategy. An array is recursively divided into halves which are sorted quite fast and easily and then the divided
pieces are merged together to give the final sorted array. 
NOTE: The time complexity (in all the cases - worst, average, and the best): O(NlogN)

Argument(s): An array (a list or a numpy array of integers)
Returns: The sorted version of the given array
"""
import numpy as np
def mergeSort(array):
    if (len(array) > 1):
        middle_index = len(array) // 2
        # Splitting the given array into two halves
        left_half = np.array(array[:middle_index])
        right_half = np.array(array[middle_index:])

        # Recursively sorting the right and left halves
        mergeSort(left_half)
        mergeSort(right_half)

        # Implementing the "conquer" part of the divide-and-conquer strategy i.e. sorting the most-divided elements
        i=j=k=0
        while ((i < len(left_half)) and (j < len(right_half))):
            if (left_half[i] <= right_half[j]):
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Checking to see if there are any left out unsorted elements
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array

if __name__ == "__main__":
    size = int(input("Enter how many elements you want in your array: "))
    my_array = [0]*size  # Or it can be directly initialized as a NumPy array with zeroes with the command:- my_array = np.zeros((size,)). Then, no need of the line my_array = np.array(my_array)
    for i in range(size):
        my_array[i] += int(input("my_array["+str(i)+"]: "))  # Taking the elements as inputs directly from the user
    my_array = np.array(my_array)
    print("The array (presumably unsorted) given is:\n", my_array)
    sorted_array = mergeSort(my_array)
    print("The sorted array is:\n", sorted_array)

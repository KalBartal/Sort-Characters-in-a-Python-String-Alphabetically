from heapq import merge


def merge_sort(string):
    # Base case
    if len(string) == 1:
        return string
    # Split the string in half
    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]
    # Sort the left and right halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = ""
    left_index = 0
    right_index = 0
    # Compare the left and right strings, character by character
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged += left[left_index]
            left_index += 1
        else:
            merged += right[right_index]
            right_index += 1
    # Add any remaining characters from either string
    merged += left[left_index:]
    merged += right[right_index:]
    return merged


string = "python"
sorted_string = merge_sort(string)
print(sorted_string)  # prints "hnopty"

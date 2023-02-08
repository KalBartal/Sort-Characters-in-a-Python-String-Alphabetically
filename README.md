# Sorting Characters in a Python String Alphabetically

[ ![Sorting Characters in a Python String Alphabetically](./image.png)](https://youtu.be/Pi1ulqplSjM)

This repository provides code for sorting characters in a Python string in alphabetical order. The code has a Time Complexity of O(n log n) and a Space Complexity of O(1). 

I have a video walkthrough of this challenge available on my [YouTube channel](https://youtu.be/Pi1ulqplSjM) and [my blog](https://kalbartal.net/sort-characters-in-a-python-string-alphabetically/).

## Getting Started 
The solution code is an example of how to solve this problem using the merge sort algorithm. Merge sort is optimal in this case since it has a time complexity of O(n log n) and a constant space complexity.

## Prerequisites
* Understanding of manipulating strings with Python
* Experience with sorting algorithms like insertion sort and merge sort
* Knowledge of the time and space complexities of each sorting algorithm

## Running the Code
The file `main.py` contains the solution code. To run the code, open the file using your text editor and run the code. 

### Break down into parts
The code is composed of two parts:
1. A recursive function called `merge_sort()` which will sort the characters in our string 
2. A function called `merge()` which merges two sorted halves of our string

## Example Output
Here is an example of the code's output when given the string "python": 

Input: "python"
Output: "hnopty"
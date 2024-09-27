def selection_sort(arr, target): #focus to find all min number after
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

#Time complexity = O(n^2)
#Space complexity = O(1)

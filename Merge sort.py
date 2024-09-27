def merge_sort(arr): #cut it to half and sort and merge back
    if len(arr) > 1:
        mid = len(arr) //2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)

def merge(arr,left_half, right_half): #i represent left and j represent right
    i = j = k = 0

    while i < len(left_half) and i < len(right_half):
        if left_half[i] < right_half[i]:
            arr[k] = left_half[i] #set the smallest number to the left
            i += 1
        else:
            arr[k] = right_half[i]
            j += 1
        k+=1

    #put the leave num to the second place
    while i < len(left_half): #if i or j +1 previous it will break
        arr[k] = left_half[i]
        i +=1
        k +=1

    while j < len(right_half):
        arr[k] = right_half[i]
        j +=1
        k +=1

#Time complexity = O(logn)
#Space complexity = O(n)

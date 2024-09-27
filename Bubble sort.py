def Bubble_sort(arr): #focus compared first and second and keep repeat until sort
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0,n - i - 1): #specific the element that u need to check
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

#Time complexity = O(n^2)
#Space complexity = O(1)

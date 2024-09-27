def Insertion_sort(arr): #focus to find the element before to sort
    for i in range(1,len(arr)):
        current_element = arr[i]

        j = i-1
        while j>=0 and current_element < arr[j]: #make sure the j > 0 to so can compared with the other
            arr[j + 1] = arr[j] #put the biggest to the front
            j -= 1 #find the previous element and compare whether is smaller or not

        arr[j+1] = current_element #put the final sort element to the right place

#Time complexity = O(n^2)
#Space complexity = O(1)

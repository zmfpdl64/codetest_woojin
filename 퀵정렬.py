array = [7,5,9,0,3,1,6,2,4,8]

def quick_sorted(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    while left <= right:
        while left <= end and array[pivot] > array[left] :
            left += 1
        while array[pivot] <= array[right] and right > start:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sorted(array, start, right-1)
    quick_sorted(array, right +1, end)
    
quick_sorted(array,0, len(array)-1)
print(array)

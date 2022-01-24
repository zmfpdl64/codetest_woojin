array = [5,7,9,0,3,1,6,2,4,8]

def  quick_sorted(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    arr = array[1:]

    left_side = [x for x in arr if pivot >= x]
    right_side = [x for x in arr if pivot < x]

    return quick_sorted(left_side) + [pivot] + quick_sorted(right_side)
print(quick_sorted(array))
# right_side [7, 9, 6, 8] [5] left_side [0, 3, 1, 2, 4]
# right_side [[6],[7],[9,8]] left_side [[0], [3,1,2,4]]
# right_side [[6],[7],[8],[9]] left_side [[0],[[1,2],[3],[4]]
# right_side [[6],[7],[8],[9]] left_side [[0],[1],[2],[3],[4]] 

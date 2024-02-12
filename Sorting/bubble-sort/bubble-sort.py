def bubble_sort(a):
    swapped = False
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j] , a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return  a

# Test the function
print("bubble_sort:", bubble_sort([5, 2, 4, 1, 3]))


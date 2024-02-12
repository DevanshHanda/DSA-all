def selection_sort(a):
    for i in range(len(a)):
        min_idx=i
        for j in range(i+1,len(a)):
            if a[j]<a[min_idx]:
                min_idx = j
            a[min_idx],a[i]=a[i],a[min_idx]
    return a

# Test the function
print('selection_sort:',selection_sort([45,23,67,98,12])) 
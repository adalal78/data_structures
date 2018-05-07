def merge_sort(alist):
    
    length = alist.shape[0]
    sorted_list = np.zeros((alist.shape[0]), dtype = int)
    
    #break alist into two lists
    left_list = alist[:length/2]
    right_list = alist[length/2:]
    
    if (left_list.shape[0] > 1):
        left_list = merge_sort(left_list)
    if (right_list.shape[0] > 1):
        right_list = merge_sort(right_list)
    
    i = 0
    j = 0
    k = 0
    
    while( i < left_list.shape[0] and j < right_list.shape[0]):
        if(left_list[i] <= right_list[j]):
            sorted_list[k] = left_list[i]
            i += 1
        else:
            sorted_list[k] = right_list[j]
            j += 1
            
        k += 1
    
    while(i < left_list.shape[0]):
        sorted_list[k] = left_list[i]
        i += 1
        k += 1
    
    while(j < right_list.shape[0]):
        sorted_list[k] = right_list[j]
        j += 1
        k += 1

    return sorted_list

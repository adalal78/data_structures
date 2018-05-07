def quick_sort(list2sort):
    
    
    if(list2sort.shape[0] > 1):
        #choose the first element as pivot value
        pivot = list2sort[0]
    
        #setup left and right runners
        left_runner = 1
        right_runner = list2sort.shape[0]-1
        
        #converge at "split point"
        while( left_runner <= right_runner):
            if(list2sort[left_runner] > pivot and list2sort[right_runner] < pivot):
                #print("Was", pivot, left_runner, right_runner)
                list2sort[left_runner], list2sort[right_runner] = list2sort[right_runner], list2sort[left_runner]
                right_runner -= 1
                left_runner += 1
                #print("Update",pivot, left_runner, right_runner)
                #print("")
                
            elif(list2sort[left_runner] > pivot and list2sort[right_runner] >= pivot):
                #print("Was",pivot, left_runner, right_runner)
                right_runner -= 1
                #print("Update",pivot, left_runner, right_runner)
                #print("")
                
            elif(list2sort[left_runner] <= pivot and list2sort[right_runner] < pivot):
                #print("Was", pivot, left_runner, right_runner)
                left_runner += 1
                #print("Update",pivot, left_runner, right_runner)
                #print("")
                
            else:
                #print("Was", pivot, left_runner, right_runner)
                left_runner += 1
                right_runner -= 1
                #print("Update",pivot, left_runner, right_runner)
                #print("")
    
        #swap pivot with "split point" given by right_runner
        list2sort[0], list2sort[right_runner] = list2sort[right_runner], list2sort[0]
        #print("right_runner", right_runner)
        #print("list2sort", list2sort)
        
        #finally recurse on the list to the weakly left or right_runner and to the right of right_runner
        left_list = list2sort[:right_runner+1]
        right_list = list2sort[right_runner+1:]
        #print("left_list", left_list)
        #print("right_list", right_list)
        
        left_list_sorted = quick_sort(left_list)
        right_list_sorted = quick_sort(right_list)
        #print("left_list_sorted", left_list_sorted)
        #print("right_list_sorted", right_list_sorted)
        #print("")
        
        sorted_list = np.append(left_list, right_list)
        return sorted_list
        
    else:
        return list2sort

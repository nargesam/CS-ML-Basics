def merge_sorthelper( arr):
        
     
        if len(arr) <= 1: 
            return

        mid = len(arr) // 2
        # print(start, mid, end )
        left = arr[:mid]
        right = arr[mid:]
        print(left, right)

        merge_sorthelper(left)
        merge_sorthelper(right)
        
        i, j, k,end  = 0 , 0, 0 , len(right)
        # _s = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else: 
                arr[k] = right[j]
                j += 1
            k += 1


        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        # if i < len(left): 
        #     for k in range(i, len(left)):
        #         arr.append(left[k])
        
        # if j < len(right): 
        #     for k in range(j, len(right)):
        #         arr.append(right[k])
        return arr


def merge_sort(arr):
    
    return merge_sorthelper(arr )



if __name__=='__main__':

    # a = ['8','2','5','6','2','4']
    a = [4,3, 2]
    print(merge_sort(a))
    # Sort(a, kind='insertion')

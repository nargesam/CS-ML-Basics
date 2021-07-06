
import random

class Sort():

    """
    kinds = selection, 

    In *selection*, at every index i, arr[0:i] is sorted. 
    for sorting questions that only you need to sort first K elements
    is really usefull. (O(N2), if k firts: O(KN), k gets closer to N not good ) in place, and NOT stable 
    """

    def __init__(self, arr, kind='selection'):
        
        func_map = {
            'selection': self.selection_sort,
            'insertion': self.insertion_sort,
            'merge': self.merge_sort,
            'quick': self.quick_sort
        }

        self._arr = func_map[kind](arr)
        print(self._arr)
    

    def __swap(self, arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


    def selection_sort(self, arr):
        min_ = 0
        for i in range(len(arr)):
            min_ = i
            for j in range(len(arr) -1, i, -1):

                if arr[j] <= arr[min_]:
                    min_ = j
            self.__swap(arr, i, min_)
        return arr
            

    def bubbleSort(self):
        pass
    
    def insertion_sort(self, arr):
        #  iterrative implementation
        #  1,2, 4,7,3(j),2==nth

        if len(arr) <= 1: return arr
        
        for n in range(1, len(arr)):
            nth = arr[n]
            j = n-1

            while j >= 0 and arr[j] >= nth:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = nth
        return arr
    


    def merge_sort(self, arr):
        
        if len(arr) <= 1: 
            return 
        
        mid = (len(arr)) // 2
        # print(mid)

        L = arr[:mid]
        R = arr[mid:]

        self.merge_sort(L)
        self.merge_sort(R)
        
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        
        return arr

    def quick_sort_helper(self, arr, start, end):
        
        if start >= end: 
            return
        
        randidx = random.randint(start, end)
        self.__swap(arr, randidx, end)

        pivot = arr[end]
        smaller = start
        # bigger = start

        for bigger in range(start, end):
            if arr[bigger] <= pivot:
                self.__swap(arr, smaller, bigger)
                smaller += 1

        
        print(arr, start, end, smaller, pivot)
        self.__swap(arr, smaller, end)

        self.quick_sort_helper(arr, start, smaller - 1)
        self.quick_sort_helper(arr, smaller+1 , end)

        return arr

    
    def quick_sort(self, arr):
        return self.quick_sort_helper(arr, 0, len(arr) - 1)


if __name__=='__main__':

    a = ['8','2','5','6','2','4']
    a = [3,4,5,6,1,2]
    Sort(a, kind='quick')
    # Sort(a, kind='insertion')

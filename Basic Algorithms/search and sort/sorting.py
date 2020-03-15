
class sort():
    def __init__(self):
        pass

    def selectionSort(self, nums):
        # self.nums = nums

        for i  in range(len(self.nums)):
            min_i = i
            for j in range(i+1, len(self.nums)):
                if  self.nums[j] < self.nums[min_i]:
                    min_i = j
            self.nums[i], self.nums[min_i] = self.nums[min_i], self.nums[i]
        return self.nums

    def bubbleSort(self, nums):
        # self.num = nums
        for i in range(len(self.num)):
            for j in range(i+1, len(self.num)):
                if self.num[i] > self.num[j]:
                    self.num[i], self.num[j] = self.num[j], self.num[i]
        return self.num
    
    def mergeSort(self, num1):
        # self.num1 = num1
        arr = num1
        # if len(arr) >1: 
        #     mid = len(arr)//2 #Finding the mid of the array 
        #     L = arr[:mid] # Dividing the array elements  
        #     R = arr[mid:] # into 2 halves 
    
        #     self.mergeSort(L) # Sorting the first half 
        #     self.mergeSort(R) # Sorting the second half 
    
        #     i = j = k = 0
            
        #     # Copy data to temp arrays L[] and R[] 
        #     while i < len(L) and j < len(R): 
        #         if L[i] < R[j]: 
        #             arr[k] = L[i] 
        #             i+=1
        #         else: 
        #             arr[k] = R[j] 
        #             j+=1
        #         k+=1
            
        #     # Checking if any element was left 
        #     while i < len(L): 
        #         arr[k] = L[i] 
        #         i+=1
        #         k+=1
            
        #     while j < len(R): 
        #         arr[k] = R[j] 
        #         j+=1
        #         k+=1
        # print(arr)
        # self.num1 = num1
        # if len(self.num1) > 1:
        #     mid = len(self.num1)//2
        #     L = self.num1[:mid]
        #     R = self.num1[mid:]
        
        #     self.mergeSort(L)
        #     self.mergeSort(R)

        #     i=j=k=0
            
        #     while i<len(L) and  j<len(R):
        #         if L[i] < R[j]:
        #             self.num1[k] = L[i]
        #             i+= 1
        #         else:
        #             self.num1[k] = R[j]
        #             j += 1
        #         k += 1
            
        #     while i < len(L):
        #         self.num1[k] = L[i]
        #         i+= 1
        #         k+= 1
        #     while j < len(R):
        #         self.num1[k] = R[j]
        #         j += 1
        #         k+= 1

        arr = num1
        print(arr)
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
        
            self.mergeSort(L)
            self.mergeSort(R)

            i=j=k=0
            
            while i<len(L) and  j<len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+= 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                arr[k] = L[i]
                i+= 1
                k+= 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k+= 1
        print(arr)

if __name__ == "__main__":

    model = sort()
    nums =  [1,6,9,3,6,9,1,0,5]

    # print(model.bubbleSort(nums))
    # print(model.selectionSort(nums))
    model.mergeSort(nums)

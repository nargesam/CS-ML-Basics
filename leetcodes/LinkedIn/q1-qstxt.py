"""
1- Given two strings(representing 2 numbers), 
task is to return sum of these numbers and return as string. 
While problem is straight forward, there were alot of edge cases: 
like number could be decimal 

("3.14"+"2.2") or big numbers may have commas 
("100,000" + "1")


"""

import unittest

class sumOfStrings():
    def __init__(self, num1, num2):
        if ',' in num1: 
            num1 = num1.replace(',', '')
        if ',' in num2: 
            num2 = num2.replace(',', '')
        
        self.num1_float=False
        self.num2_float=False

        if '.' in num1: 
            num1, num1fl = num1.split('.')
            self.num1_float=True

        if '.' in num2: 
            num2, num2fl = num2.split('.')
            self.num2_float=True

        self.num1 = num1
        self.num2 = num2
        
        # TODO: check if there are . or , in the number 
        #   if , you can simply replace it. DONE 
        # TODO: if . then you can sum the before and after float seperately, and add 1 if float summ has carry 
        


    def sum(self):

        if self.num1_float == False and self.num2_float==False: 
            minlen = min(len(self.num1), len(self.num2))
            maxlen = max(len(self.num1), len(self.num2))

            zeros = maxlen - minlen

            if minlen == len(self.num1):
                self.num1 = '0'*zeros + self.num1
            if minlen == len(self.num2):
                self.num2 = '0'*zeros + self.num2

            assert len(self.num1) == len(self.num2)

            one = self.num1[::-1]
            two = self.num2[::-1]
            total =  _sum_two(one, two)
            # run sum_nums
        elif self.num1_float or self.num2_float:
            pass
            # run sum_nums and append the float part to the final sum
        else: 
            pass
            

            # sum the float parts, save the f_carry 
            # sum the int part, start the summ with carry=1 if f_carry = 0  

        # print(total)
        return int(''.join([str(i) for i in total[::-1]]))
    
    def _sum_two(self, one, two):
            

            i=0
            carry = 0
            total = []

            for i in range(maxlen):
                curr = int(one[i]) + int(two[i]) + carry
                
                if curr >= 10: 
                    carry = 1 
                else: 
                    carry = 0

                total.append(curr%10)
                # print(i, curr, carry , curr%10, total )

                i += 1
            
            if carry == 1: 
                total.append(1)

print(sumOfStrings('10,000', '121').sum())
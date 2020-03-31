# You have a set of users visiting your website. Each user picks a color represented by RGB. R, G, B can take values between 0 and 255.

# You have a stream of users coming and at any point you have to calculate the mean and median for RGB colors seen so far.

# Example:

# setRGB(), red, green, blue, {0, ..., 255}
# showMean()
# showMedian()
# RGB                 Mean                Median
# (0, 0, 0),        (0, 0, 0)              (0, 0, 0)
# (34, 232, 9), (17, 116, 4.5)   (17, 116, 4.5)
# (43, 21, 34), (77/3, .., ..)        (34, 21, 9)

class getMinMedianVisitors:
    def __init__(self):
        self.sum_red = 0
        self.sum_blue = 0
        self.sum_green = 0
        self.num_visitors = 0

        # O(256) space complexity
        self.red_freq = [0]*256
        self.green_feq = [0]*256
        self.blue_freq = [0]*256

    def setRGB(self, RGB):
        r, g, b = RGB
        
        # for median
        self.red_freq[r] +=1
        self.green_freq[g] += 1
        self.blue_freq[b] += 1
        
        # for mean
        self.sum_red  += r
        self.sum_green += g
        self.sum_blue  += b
        self.num_visitors += 1
        
    def showMean():
        # O(1)
        if self.num_visitors == 0:
            return 0,0,0
        return self.sum_red/self.num_visitors, \
                self.sum_green/self.num_visitors,\
                self.sum_blue/self.num_visitors


    def showMedian():
        # O(n) n being the # of visitors

        def find_median(color_freq, median_idx):
            sum_cnt = 0
            for idx, freq in color_freq:
                if freq > 0:
                    sum_cnt += freq

                    if median_idx <= sum_cnt - 1:
                        return idx

        if self.num_visitors%2 == 1: 
            mid_index = self.num_visitors//2
            median_red = find_median(self.red_freq, mid_index)
            median_green = find_median(self.green_feq, mid_index)
            median_blue = find_median(self.blue_freq, mid_index)
        else: 
            mid_index1 = self.num_visitors//2
            mid_index2 = self.num_visitors//2 - 1
            
            median_red = (find_median(self.red_freq, mid_index1) + \
                            find_median(self.red_freq, mid_index2)) /2
            median_green = (find_median(self.green_feq, mid_index1) + \
                            find_median(self.green_feq, mid_index2)) /2
            median_blue = (find_median(self.blue_freq, mid_index1)+ \
                            find_median(self.blue_freq, mid_index1) ) /2
            
            return median_red, median_blue, median_green


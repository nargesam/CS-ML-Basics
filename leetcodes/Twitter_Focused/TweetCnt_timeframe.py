import collections
"""
enum Frequency {
        MINUTE,
        HOUR,
        DAY
    }

recordTweet("tweet1", 3498264982l (time in millis)) method is called multiple times for 
different tweetNames and times that records the time at which the tweet occurred.

For example if the tweetName tweet1 occurs five times in last 2 hours from current 
time {consider current time is 3 pm} (for e.g. 3 times in first hour {1 pm to 2 pm} and 
2 times in second hour {2 pm to 3 pm}). then the result should be following:

getTweetCountsPerFrequency(HOUR, "tweet1", <2 pm>, <3 pm>); // should return [2]
getTweetCountsPerFrequency(HOUR, "tweet1", <1 pm>, <3 pm>); // should return [3, 2]
getTweetCountsPerFrequency(HOUR, "tweet1", <1 pm>, <2 pm>); // should return [3]
getTweetCountsPerFrequency(DAY, "tweet1", <3 pm yesterday>, <3 pm today>); // should return [5]
If I were to explain the problem in more simpler way, it can be - given method 
addWord(String word, long time) records the word and at which time it occured, 
return the array of count long[] of given word occurred every min / every hour / every day 
between given range startTime and endTime.
"""

class countTweet:
    def __init__(self):
        self.tweet_dict = collections.defaultdict(list)

    def recordTweet(self,  tweetName,  time):
        self.tweet_dict[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq,  tweetName,  startTime,  endTime):
        if tweetName not in self.tweet_dict:
            return []
        
        interval_start_list = self.getGranularity(freq, startTime, endTime)

        print(interval_start_list)
        tweet_times = self.tweet_dict[tweetName]
        print(tweet_times)
        return_cnts = [0]*(len(interval_start_list)-1)

        tweet_times.sort()
        t = len(tweet_times) - 1
        j = len(interval_start_list) - 2

        while t >= 0 and j >= 0:
            
            if tweet_times[t] >= interval_start_list[j] and tweet_times[t] < interval_start_list[j+1]:
                return_cnts[j] += 1
                t -= 1

            else: 
                if tweet_times[t] > interval_start_list[j+1]:
                    t -= 1
                    continue
                else:
                    j-=1
        return return_cnts

             

    def getGranularity(self, freq, startTime, endTime):

        diff = endTime - startTime
        
        interval_start_list = [startTime]
        if freq == 'MINUTE':
            granularity_cnt = int(diff/60000) + 1 
            print(granularity_cnt)
            for i in range(granularity_cnt):
                interval_start_list.append(interval_start_list[-1] + 60000)
                if interval_start_list[-1] > endTime:
                    interval_start_list[-1] = endTime
        
        if freq == 'HOUR':
            granularity_cnt = int(diff/(60000*60)) + 1
            for i in range(granularity_cnt):
                interval_start_list.append(interval_start_list[-1] + (60000*60))
                if interval_start_list[-1]  > endTime:
                    interval_start_list[-1] = endTime

        if freq == 'DAY':
            granularity_cnt = int(diff/(60000*60*24)) + 1
            for i in range(granularity_cnt):
                interval_start_list.append(interval_start_list[-1] + (60000*60*24))
                if interval_start_list[-1] > endTime:
                    interval_start_list[-1] = endTime

        return interval_start_list


                



obj = countTweet()
obj.recordTweet("tweet1", 3498264982 ) 
obj.recordTweet("tweet1", 3498324983 ) 
obj.recordTweet("tweet1", 3498384000 ) 
obj.recordTweet("tweet1", 3498384001 ) 



# For example if the tweetName tweet1 occurs five times in last 2 hours from current 
# time {consider current time is 3 pm} (for e.g. 3 times in first hour {1 pm to 2 pm} and 
# 2 times in second hour {2 pm to 3 pm}). then the result should be following:

print(obj.getTweetCountsPerFrequency('MINUTE', "tweet1", 3498264981, 3498384002))  #; // should return [2]
# obj.getTweetCountsPerFrequency(HOUR, "tweet1", <1 pm>, <3 pm>); # // should return [3, 2]
# obj.getTweetCountsPerFrequency(HOUR, "tweet1", <1 pm>, <2 pm>); # // should return [3]
# obj.getTweetCountsPerFrequency(DAY, "tweet1", <3 pm yesterday>, <3 pm today>) #; // should return [5]

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
        self.tweet_dict = []

    def recordTweet(self,  tweetName,  time):
        MINUTE = time/60000
        HOUR = MINUTE/60
        DAY = HOUR/12
        self.tweet_dict.append((tweetName, MINUTE, HOUR, DAY))

    def getTweetCountsPerFrequency(self, freq,  tweetName,  startTime,  endTime):
        for tweet_name, minute, hour, day in self.tweet_dict:
            if tweet_name == tweetName and freq == 'MINUTE' and minute <=s:
                






recordTweet("tweet1", 3498264982l ) 
recordTweet("tweet1", 3498264982l ) 
recordTweet("tweet1", 3498264982l ) 
recordTweet("tweet1", 3498264982l ) 



# For example if the tweetName tweet1 occurs five times in last 2 hours from current 
# time {consider current time is 3 pm} (for e.g. 3 times in first hour {1 pm to 2 pm} and 
# 2 times in second hour {2 pm to 3 pm}). then the result should be following:

getTweetCountsPerFrequency(HOUR, "tweet1", <2 pm>, <3 pm>)  #; // should return [2]
getTweetCountsPerFrequency(HOUR, "tweet1", <1 pm>, <3 pm>); # // should return [3, 2]
getTweetCountsPerFrequency(HOUR, "tweet1", <1 pm>, <2 pm>); # // should return [3]
getTweetCountsPerFrequency(DAY, "tweet1", <3 pm yesterday>, <3 pm today>) #; // should return [5]
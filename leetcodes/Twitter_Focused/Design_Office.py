"""


https://leetcode.com/discuss/interview-question/373110/Twitter-or-OA-2019-or-New-Office-Design

"""

def maxHashHeight(p, h):
    
    maxHeights = []
    for i in range(len(p)-1):
        j = i+1
        if p[i] < p[j] and p[j]  - p[i] - 1 != 0:
            num_hash = p[j]  - p[i] - 1
            
            num_hash_list = [h[i]] + [float('inf') for k in range(num_hash)] +[h[j]]

            b = 0
            c = 1
            a = 2
            while a < len(num_hash_list):
                num_hash_list[c] = min(num_hash_list[a], num_hash_list[b]) + 1
                a += 1
                b += 1
                c += 1
            
            b = len(num_hash_list) - 1
            c = len(num_hash_list) - 2
            a = len(num_hash_list) - 3
            while a> 0:
                num_hash_list[c] = min(num_hash_list[a], num_hash_list[b]) + 1
                a -= 1
                b -= 1
                c -= 1
            
            for m in num_hash_list: 
                maxHeights.append(m)
    
    return max(maxHeights)
            

# p  = [1,3,7]
# h = [4,3,3]

p = [1,10]
h = [1,5]

print(maxHashHeight(p,h))



# Some C++ solution: 
"""
Here is my O(n) single scan solution assuming that position array is sorted in the input. ( if not then sort it first and then scan O(nlogn) ).
The idea is to calculate maxHeight, given two heights and empty slots between them. Two cases :
[1] If both heights are same then meet in middle.
[2] If they are not same then

[2.A] check if we can make it same by advancing smaller height further and then go back to step [1].
[2.B] we cannot make it same , then its simply small height + empty slots.


int calculateHeight( int dist, int height1, int height2 )
{
    int  minH = min( height1, height2);
    int  maxH = max( height1, height2 );
    
    if( dist == 0 ) return 0;
    if( dist == 1 ) return minH + 1;
    
    // if both heights are same then meet in middle
    if(minH == maxH )
    {
        int add = ( dist%2 == 0 ) ? dist/2 : dist/2+1;
        return minH + add;
    }
        
    // See if we can make the height same 
    int delta = maxH-minH;
    if( delta < dist )
    {
        dist -= delta;
        minH += delta;
        int add = ( dist%2 == 0 ) ? dist/2 : dist/2+1;
        return minH+add;
    }
    
    // for all cases where delta >= dist
    return minH+dist;    
}

int getMaxHeight( const vector<int>& positions, const vector<int>& heights )
{
    if( positions.empty() || heights.empty() || positions.size() != heights.size() )
    {
        return 0;
    }
    
    int result = 0;
    for(int i=1; i<positions.size(); ++i )
    {
        int currMax = calculateHeight( positions[i]-positions[i-1]-1, heights[i], heights[i-1] );
        result = max( result, currMax);
    }
    return result;
}

int main() {
    cout << getMaxHeight({1,10}, {1,5}) << endl;
    cout << getMaxHeight({1,3,7},{4,3,3}) << endl;
     cout << getMaxHeight({1,2,4,7},{4,5,7,11}) << endl;
}
"""
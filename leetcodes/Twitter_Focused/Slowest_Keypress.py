"""
given a list : [[0,1], [2,4], [0,10]] for typing 'aca': show which char 
takes the longest time to be clicked on this new keyboard. 

return c

"""

def slowestKeyPress(keypress):
    chars = [k[0] for k in keypress]

    max_press_time = {c:0 for c in chars}
    
    for i in range(1,len(keypress)):
        char = keypress[i][0]

        if keypress[i][1] - keypress[i-1][1] > max_press_time[char]:
            max_press_time[char] = keypress[i][1] - keypress[i-1][1]

    return chr(max(max_press_time, key=max_press_time.get) + 97)

    



keypress = [[0,1], [2,4], [0,10], [3,11], [3, 20]] 
print(slowestKeyPress(keypress))
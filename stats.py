# From HackerRank 30-days of Statistics

## Day 0: Mean, Median, and Mode

def mean(lst):
    sum = 0
    length = len(lst)
    
    for num in lst:
        sum += float(num)
    return float(sum / length)

def median(lst):
    lst.sort()
    half = len(lst) / 2
    
    if len(lst) % 2 == 0:
        return (float(lst[half]) + float(lst[half-1]))/2    
    
    return float(lst[half])

def mode(lst):
    num_freq = {}
    
    for num in lst: 
        if num in num_freq: 
            num_freq[num] += 1
        else: 
            num_freq[num] = 1
    inverse = [(value, key) for key, value in num_freq.iteritems()]
    max_count = max(inverse)[0]
    min_num = max(inverse)[1]
    for pair in inverse: 
        if pair[0] == max_count and pair[1] < min_num:
            min_num = pair[1]
            
    return min_num

# Test 
lst = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
print mean(lst) == 43900.6
print median(lst) == 44627.5
print mode(lst) ==4978

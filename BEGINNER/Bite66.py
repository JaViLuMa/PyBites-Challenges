def running_mean(sequence):
    N = len(sequence)
    sum = 0
    
    result = list(0 for x in sequence)
    
    for i in range(0, N):
        sum += sequence[i]
        result[i] = round((sum / (i+1)), 2)
        
    return result

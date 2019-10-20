def rotate(string, n):
    if n > 0:
        L1 = string[0:n]
        L2 = string[n:]
        
        string = L2 + L1
        
        return string
    
    else:
        R1 = string[n:]
        R2 = string[0:n]
        
        string = R1 + R2
        
        return string

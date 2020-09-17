def fin(n):
    fli = []
    
    for i in range(n):
        
        if i>=2:    
            fli.append(fli[i-1] + fli[i-2])
        else: fli.append(1)

    print(fli)

fin(17)
        

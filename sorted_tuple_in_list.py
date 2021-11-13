def last(n):
    return n[-1]

def final(tuples):
    return sorted(tuples,key = last)


a=[(1,2),(2,5),(4,3),(6,2)]
print(final(a))
    
    

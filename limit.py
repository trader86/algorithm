lis= [1,2,3,4,5,6]

def limit(arr, min=None, max=None):
    
    min_value = lambda val : True if min is None else (val <= min )
    max_value = lambda val : True if max is None else (val >= max )

    return [ val for val in arr if min_value(val) and max_value(val) ]

print(limit(lis,3))
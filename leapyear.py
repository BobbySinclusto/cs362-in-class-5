def is_leapyear(n):
    if type(n) != int:
        raise TypeError('Argument must be an integer.')
    if n < 0:
        raise ValueError('Year must be at least 0.')
    
    return True if n%4==0 and (n%400==0 or n%100!=0) else False
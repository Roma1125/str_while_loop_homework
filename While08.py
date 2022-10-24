def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    t=0
    i=0
    while t<=len(s)-1:
        if  int(s[t])%2==1:
            i+=1
        t+=1
    return i 
print(main('12345678'))

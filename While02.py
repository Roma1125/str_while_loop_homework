def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    t=0
    i=0
    while t<=len(s)-1:
        if s[t].isalpha(): 
            i+=1
        t+=1
        
      
    return i
print(main('salom1234'))
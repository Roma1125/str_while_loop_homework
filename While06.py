def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    t=0
    answer=0
    s=s.lower()
    while t<len(s):
        if s[t].isalpha and s[t]!='a' and s[t]!='e' and s[t]!='i' and s[t]!='o' and s[t]!='u' :
            answer+=1
        t+=1
    return answer
print(main('salom'))

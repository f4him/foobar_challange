
def solution(s):
    new=''
    for x in s:
        if ord(x)>=97 and ord(x)<=122:
            new+=chr(219-ord(x))
        else:
            new+=x
    
    return new
        

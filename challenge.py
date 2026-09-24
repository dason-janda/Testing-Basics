def reverseString(string):
    try:
        lp = 0
        rp = len(string)-1
        while lp < rp:
            string = string[:lp] + string[rp] + string[lp+1:rp] + string[lp] + string[rp+1:]
            lp+=1
            rp-=1
        return string
    except:
        return TypeError
    
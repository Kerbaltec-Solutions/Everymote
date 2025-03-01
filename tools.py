def get_between(t,s,e):
    start = t.find(s) + len(s)
    end = t.find(e, start)
    if(end == -1):
        return(t[start:])
    return(t[start:end])

def replace(t):
    return(t.replace("? ", " ").replace('%20', ' ').replace('+', ' ').replace('%23', '#')).replace('%2B', '+')
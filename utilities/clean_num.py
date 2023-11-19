import numpy as np

def clean_num(a):
    if isinstance(a,str):
            a=a.lower()
            a=a.replace(',','')
            a=a.replace('(','-')
            a=a.replace(')','')
            a=a.replace('x','')
            a=a.replace('e','')
            a=a.replace('a','')
            a=a.replace('+','')
            a=a.replace('%','')
            
            try:
                a=float(a)
            except:
                a=a
    
    return a
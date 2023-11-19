import re
import numpy as np




def get_index_from_list(List,key_word,Title=True,last_element=True):
    if last_element==False:
        index=[]
    for element in List:
        i=str(element)
        if Title==True:
            
            i_modified=i.replace('(','')
            i_modified=i_modified.replace(')','')
            word=re.findall(key_word,i_modified.title())
        else:
            i_modified=i.replace('(','')
            i_modified=i_modified.replace(')','')
            word=re.findall(key_word,i_modified)
        if len(word)!=0:
            if last_element==True: 
                index=List.index(element)
            else:
                index.append(List.index(element))
    
    try:
        return index
    except:
        return np.nan
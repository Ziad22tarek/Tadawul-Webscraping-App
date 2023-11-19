from utilities.clean_num import clean_num
import numpy as np




def clean_row(row,num_col):

    count=0
    modified_row=[]
    for element in range(len(row)):
        if isinstance(clean_num(row[element]),str):
            
            for error_elemnt in row[element].split():
                # if clean_num(error_elemnt)=='-':
                #     modified_row.append(np.nan)
                if clean_num(error_elemnt)=='--':
                    modified_row.append(np.nan)
                elif clean_num(error_elemnt)=='_':
                    modified_row.append(np.nan)
                elif clean_num(error_elemnt)=='nm':
                    modified_row.append(np.nan)
                else:
                    cleannum=clean_num(error_elemnt.lower())
                    if not isinstance(cleannum,str):
                        modified_row.append(cleannum)
                count+=1
        else:
            if clean_num(row[element])=='-':
                    modified_row.append(np.nan)
            elif clean_num(row[element])=='--':
                    modified_row.append(np.nan)
            elif clean_num(row[element])=='_':
                modified_row.append(np.nan)
            elif clean_num(row[element])=='nm':
                modified_row.append(np.nan)
            else:
                modified_row.append(clean_num(row[element].lower()))
            count+=1
        if count==num_col:
            break 
    
    
    return modified_row 
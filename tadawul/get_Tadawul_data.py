import fitz
import pandas as pd
from utilities.clean_row import clean_row
import datetime
import re



def get_Tadawul_data(file_name):
    ''' Afunction that extract data from tadawul pdf report


    Parametars
    -----------

    file_name: str
        Tadawul Report Name


    Return
    --------

    A DataFrame that cotains the data we want
    '''



    # Get the foldar path that has the reports
    pdf_location=r'.\Tadawul Reports'


    # Read the file
    fitz_pdf=fitz.open(pdf_location+'\\'+file_name)

    # Get The Date From Report Name
    date=''
    try:
        date=re.findall(r'\d{1,2}\D\d{1,2}\D\d{4}',file_name)
        date=date[0]
        ## Convert the date to datetime type
        date=datetime.datetime.strptime(date,'%d-%m-%Y')
    
       
    
    except:
        date=re.findall(r'\d+',file_name)
        date=date[0]
        date=datetime.datetime.strptime(date,'%Y%m%d')
    
     



    # Extract the texct from all the pages
    pages={}
    for page_num in range(len(fitz_pdf)):
        pages[page_num]=fitz_pdf[page_num].get_text()


    # Modifay The pages by reomving \n and the ()
    ## Modifiny the text page by repolacing \n to white space
    modified_pages={}
    for page in pages:
        modified_pages[page]=pages[page].replace('\n',' ')
        modified_pages[page]=modified_pages[page].replace('(','-')
        modified_pages[page]=modified_pages[page].replace(')','')


    # Searching for The Page that Contains The data
    pages_list=[]
    ## Searching for the first keyWord
    for page in modified_pages:
        word=re.findall('Value Traded -by Nationality and Investor Type'.title(),modified_pages[page].title())
        if len(word)!=0:
            pages_list.append(page)


    # Define the column Headrers
    column_header=['Investor Type','Nationality','Buy','% Of Total Buys','Sell','% Of Total Sells','Net Value Traded','% Of Net Value Traded']


    # Read The file that contains the fields that we want to extract
    fields=pd.read_excel(r'.\assest_files\Tadawul Key Words.xlsx',sheet_name='Key Words')

    # Get the number of columns
    num_col=len(column_header)



    # Extract the data that we want and store it into a DataFrame
    tadawul_data=pd.DataFrame(columns=column_header)
    for page in pages_list:
        
        page_text=pages[page].splitlines()
            
        page_text=[i.strip().title() for i in page_text if i.strip() !='']

        for Nationality,Key_word in fields.values:
            if Key_word.title() in page_text:
                field_index=page_text.index(Key_word.title())
                row=page_text[field_index:field_index+num_col-1]
                row[0]=Key_word
                df_length=len(tadawul_data)
                tadawul_data.loc[df_length,'Investor Type']=row[0]
                tadawul_data.loc[df_length,'Nationality']=Nationality
                tadawul_data.loc[df_length,column_header[2:]]=clean_row(row[1:],num_col)


    # Create a Date Column
    tadawul_data['Date']=[date]*len(tadawul_data)



    return tadawul_data

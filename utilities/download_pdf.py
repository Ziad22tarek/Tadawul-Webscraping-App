import requests







def download_pdf(pdf_url,pdf_path):
    ''' A Founction That downloads PDF files for the Web


    Parameters
    ------------
    pdf_url: str
        The PDF website link

    pdf_path: str
        the folder path that you want to store the pdf in


    '''



    # Fetching the URl
    headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
    try:
        response=requests.get(pdf_url, timeout=None)
    except:
        response=requests.get(pdf_url, headers=headers,timeout=None)
    # checking if the status code is equal to 200
    if response.status_code==200:
        # Adding '.pdf' to the name of the file
        pdf_path=pdf_path+'.pdf'
        # creating a pdf file
        with open(pdf_path,'wb') as f:
            f.write(response.content)
import requests
from bs4 import BeautifulSoup


def get_tadawul_pdf_links(pdf_type_list,years,months=list(range(1,13))):
    '''A Function that gets the pdf links that you want from tadawul website


    Parameters
    ------------

    year: list
        list of the year that you want to take its reports

    year: list
        list of the months that you want to take its reports


    pdf_type: list
        list of the pdf type whether it's a Monthly report or Weekly report



    Return
    ----------
    A dectionary its keys the report names and its values are the pdf link

    '''

    
    # Creating a list to store the names of the files
    pdf_names={}    

    # Create a variable to store the link of the website that i want to scrape
    url='https://www.saudiexchange.sa/wps/portal/saudiexchange/newsandreports/reports-publications/annual-reports?locale=en'
    # Fetching the URl
    respons=requests.get(url)
    # Geting the content from the website
    src=respons.content
    # Create a soup object to parse the content
    pagesoup=BeautifulSoup(src,'lxml')

    # Searching of the files in Trading by Nationality
    for type in pdf_type_list:
        for year in years:
            for month in months:
                if len(str(month))==1:
                    trading=pagesoup.find_all('li',{'id':f'{year}_0{month}_SA-TradingByNationality'})
                else:
                    trading=pagesoup.find_all('li',{'id':f'{year}_{month}_SA-TradingByNationality'})
                if trading:
                    for i in range(len(trading)):
                        name=trading[i].find('h2').text
                        if name[:len(type)]==type:
                            # Searching for a attributes to get the links
                            link=trading[i].find('a').get('href')
                            # Adding 'https://www.saudiexchange.sa/' to the link
                            link='https://www.saudiexchange.sa/'+link

                            pdf_names[name]=link


    return pdf_names

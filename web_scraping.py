import requests
import html5lib
from bs4 import BeautifulSoup
import asyncio
import smtplib

class Webscrapping:
    
    base_url= "https://stocks.zerodha.com/stocks/"

    def get_data():
        try:
            company_code= input("Type the company code ")
            url= Webscrapping.base_url+company_code
            html_data= requests.get(url)
            soup = BeautifulSoup(html_data.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
            price= soup.find("span",class_="jsx-2945882850 current-price text-dark text-24")
            name= soup.find("h1",class_="jsx-1009106679 typography-h5 security-name")
            if(type(price) is type(None)):
                return ('error')
            return ({'price':price.text,'name':name.text})
        except Exception as e:
            print(e)
    
    #email feature
    '''content="Hello World"
    mail=smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender='pransanjitnagesh@gmail.com'
    recipient='prasannachat@gmail.com'
    mail.login('prasanjitnagesh@gmail.com','dbhyvvtuhjgraoos')
    header='To:'+'\n'+'From:' \
    +sender+'\n'+'subject:testmail\n'
    content=header+content
    mail.sendmail(sender, recipient, content)
    mail.close()
    '''
    

    




        
       


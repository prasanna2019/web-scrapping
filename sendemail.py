import smtplib
import re
def email(data):
    print(data['name'])
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emailid= input("Enter an email address to get info ")
    while(re.fullmatch(regex, emailid) == None):
        emailid= input("Enter an email address to get info ")    
    
    try:
        mail=smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        sender='pransanji1tnagesh@gmail.com'
        content= 'Stock price of '+data['name']+' is Rs.'+data['price']
        mail.login('prasanjitnagesh@gmail.com','dbhyvvtuhjgraoos')
        header='To:'+'\n'+'From:' \
        +sender+'\n'+'subject:Stock price\n'
        content=header+content
        mail.sendmail(sender, emailid, content)
        mail.close()
    except Exception as e:
        print(e)
    
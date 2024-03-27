from web_scraping import Webscrapping
from sendemail import email
def run():
    data= Webscrapping.get_data()
    if(data != 'error'):
        email(data)
    print(data)




if __name__ == "__main__":
    run()


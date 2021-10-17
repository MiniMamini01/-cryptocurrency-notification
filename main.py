import requests
from plyer import notification
import time
import datetime

def arz(self):
    url = f'https://coinmarketcap.com/currencies/{self}/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    return html

def Price(curencie):
    html = arz(curencie)
    a = 'class="priceValue "'
    find_value = html.find(a)
    len_value = len(a)
    start = find_value + len_value + 2
    length = html[start:start+30]
    m = length.find('</div>') + start
    price = html[start:m]
    if price =='':
        print("it's wrong ; please enter correct currencie")
        

    return price

def alert(self,resistance,support):
    x = Price(self)
    b = None
    if x >= resistance:
        b = 'Price breaks the resistance'
        
    elif x <= support:
        b = 'Price rejected the support'
        

    return b 

def Notify(a,b,c):
        #a = your currencie
        #b = resistance
        #c = supprot
        
        event = alert(a,b,c)
        price = Price(a)
        if event != None:

            notification.notify(
                
                title = f"Opps .. New Event , the {a} price is {price} on {datetime.date.today()}",
                message = event,
                app_icon = 'fuck.ico',
                timeout =50 
            )
            title = f"Opps .. New Event , the {a} price is {price} on {datetime.date.today()}"
            with open('notification.txt','a') as notif:
                notif.write(f"\nTitle: {title}\nmessage: {event}")
        else:
            pass    

def exit():
    with open('what.txt','r') as content :
        data = content.read().strip()
        if data == 'quit':
            print('we exit the program')
            notification.notify(

                title = 'we exit the program , have a good day mostafa',
                message = 'none',
                app_icon = 'fuck.ico',
                timeout =50 
            )
            quit()

            

while True:
    try:
        Notify('bitcoin','51,615.60','53,571.36')
        time.sleep(5)
        Notify('ethereum','2,708.91','3,450.57')


        time.sleep(5)
        exit()
        time.sleep(60)
    except Exception:
        print('please check internet connection')
        exit()






def SendSms(number, text):
    from textmagic.rest import TextmagicRestClient
    
    username = "your_textmagic_username"
    token = "your_apiv2_key"
    client = TextmagicRestClient(username, token)
    
    message = client.messages.create(phones = number, text = text)
    return True
    

def SendMail(email, text):
    import smtplib
    
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail('from@alif.tj', email, text)
    print("Успешно")
    return True
    
    
def Main():
    from models import Client, Product, Event
    import sys
    print(sys.argv)
    d = {}
    
    for i in sys.argv:
        if i.startswith('type-'):
            TypeOfMsg = i[5:]
        elif i.startswith('client-'):
            Clientid = i[7:]
        elif i.startswith('product-'):
            Productid = i[8:]
    clnt = Client.select().where(Client.id == Clientid).get()
    prdct = Product.select().where(Product.id == Productid).get()
    text = '''Здравствуйте, Вы купили {} стоимостью {}'''.format(prdct.name, prdct.cost)
    res = False
    if TypeOfMsg.lower() == 'sms':
        res = SendSms(clnt.phone, text)
    elif TypeOfMsg.lower() == 'mail':
        res = SendMail(clnt.email, text)
    if res:
        e = Event(product = prdct, client = clnt)
        e.save()

Main()

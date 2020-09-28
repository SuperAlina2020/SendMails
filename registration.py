import sendgrid
from sendgrid import Mail,Email,Content
sendgrid_api_key = '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'
SUBJECT = 'Hello'
sg = sendgrid.SendGridAPIClient(sendgrid_api_key)

def send_email(email,code):
    body = 'best code='+code
    message = Mail(
        from_email='maximneveraa@gmail.com',
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=body,
        )
    response = sg.send(message)


def registration(username,password,check_password):
    global code

    code = '12345'

    if password == check_password:
        send_email(username,code)
    else:
        print('Повторите попытку')
registration("emma.apigrid@gmail.com","12345","12345")



strings = ['Samsung j5',
           'samsung galaxy',
           'iphone 10',
           'iphone 5S',
           'samsung a9'
           'ASUS-Roc',
           'Acer HyperX',
           'Macbook Air 18',
           'Macbook Pro 18',
           'geforce gtx460',
           'HDD 1TB',
           'SSD Adata 3100/1400mbs',
           'HDD 2TB',
           'Mac 19',
           'amd Ryzen 490',
           'GeForce TI 2020',
           'SSD Kingston 512 gb',
           'SSD Adata 1TB',
           'Acer zenbook',
           'Asus razer'
           ]
def file_strings(strings):
    with open('goods.txt','a') as file1:
        for sentence in strings:
            file1.write(sentence.lower()+'\n')
file_strings(strings)

def sort_of():
    f = open('goods.txt')
    fp = f.readlines()
    for sen in fp:
        if 'samsung' or 'iphone' in sen:
            with open('phones.txt','a') as f2:
                f2.write(sen)
        elif 'acer' or 'asus' or sen.startswith(mac) in sen:
            with open('comp.txt','a') as f3:
                f3.write(sen)
        elif 'amd' or 'geforce' in sen:
            with open('proc.txt','a') as f4:
                f4.write(sen)
        elif 'hdd' or 'ssd' in sen:
            with open('disk.txt','a') as f5:
                f5.write(sen)
    f.close()
sort_of()

def open_file(filename):
    with open(filename,'r') as f1:
        var = f1.read()
    return var
open_file(filename='phones.txt')

a = input("Введите товар :")
if a == 'phones':
    open('phones.txt','r')
elif a == 'computers':
    open('comp.txt','r')
elif a == 'processors':
    open('proc.txt','r')
elif a == disks:
    open('disk.txt','r')
print(a)

import requests
API_key = 'af23013bed5641e6efb2a3752b022b85-aff2d1b9-f98d761b'
API_base_URL = 'https://api.mailgun.net/v3/sandboxac90d724369947c3a09edf9850795e19.mailgun.org/messages'

def send_email(API_key, API_base_URL,store_list,total_sum):
    response = requests.post(

        API_base_URL,
        auth=("api", API_key),
        data={"from": "alina.turganbaeva2019@gmail.com",
              "to": ["maximneveraa@gmail.com", ],
              "subject": "Hello from Internet Store",
              "text": [store_list,'Общая сумма покупки',total_sum]})
    print(response)
    return response



catalogue = {'microphone':1500,'air-pods':4000,'beats':8000,
             'samsung a5': 10500,'Acer ASPIRE e15': 30000,
             'hard drive':6400,'iphone 8s': 16000,'iphone X': 40000,
             'mouse RX7':8000,'hikvision laland':2280,'kocom': 3990,
             'HIKVISION DS-KD-DIS': 5410, 'commaX cdv':9560,
             'TP-LINK TL-WR841N':1450,'hoco m60': 120,
             'SVEN ap':290,'panasonic': 32460,'Falcon sdd ADATA':6650,
             'Apple Watch':8000

             }

def login(username,password):
    if len(username) < 20 and not password.isalpha() and not password.isdigit():
        return True

    return False

def counter(money,price):
    if money > price:
        result = money - price
        return result
    else:
        return 'У вас недостаточно средств!'

store_list = []
num = 2
def cartage():

    for i in range(2):
        product = input('Выберите товар')
        store_list.append(product)
    return store_list
cartage()
purchase = cartage()
print(cartage(),"Товары добвылены в каталог")

final_list = []
for i in purchase:
    final_list.append('Вы купили товар :'+ i)

user_name = 'alina123'
password = 'user12345'
user_check = input('Введите имя пользователя:')
password_check = input('Введите пароль:')


def buy(store_list):
    if login(username='alina123',password='user12345'):
        money = int(input('Введите количество средств:'))
        all_money = money
        for purchase in store_list:
            if purchase in catalogue:

                key_price = catalogue[purchase]
                money = counter(money,key_price)
                result = all_money-money
        send_email(API_key=API_key,API_base_URL=API_base_URL,store_list=final_list,total_sum=result)

        return money
    else:
        return 'Зайдите в систему'

print(buy(store_list))
















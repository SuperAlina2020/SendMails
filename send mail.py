import sendgrid
from sendgrid import Mail,Email,Content
sendgrid_api_key = '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'
SUBJECT = 'Hello'
sg = sendgrid.SendGridAPIClient(sendgrid_api_key)



strings = ['Hello Emma it"s Mark how are u, i need your help!',
           'Hello Marty it"s Mark how are u, i need your help!',
           'Hello Mark it"s Mark how are u, i need your help!',
           'Sales! Li-ning sales!','Buy Right now',
           'Hello Emma, how do u do?Im gonna invite u to restaurant',
           'Hello Emma how are u? Have a nice day',
           'EMMA SOS!!! Production is down','Sales in Nike shop',
           'Emma hello, help me pls',
           'Hi Emma, its Marty McFly i want invite u to time-travel',
           'Hi, Emma, please, need to meet']

def file_of_string(strings):
    with open('textsend.txt','a') as file1:
        for sentence in strings:
            file1.write(sentence.lower()+'\n')
file_of_string(strings)


def read_to():
    with open('textsend.txt','r') as file2:
        files1 = file2.readlines()
        for sen in files1:
            if sen.startswith('buy right now!') or sen.startswith('sales'):
                with open('spam.txt','a') as f1:
                    f1.write(sen)
            elif "emma" in sen and "help" not in sen and "sos" not in sen and "dear" not in sen:
                with open('emma.txt','a') as f2:
                    f2.write(sen)
            elif "help" or "sos" or "dear" in sen:
                with open('stev.txt','a') as f3:
                    f3.write(sen)
read_to()

def sendgrid_email_emma():
    with open('emma.txt','r') as f4:
        emma_list = f4.readlines()
        for line in emma_list:
            body = line
            message =Mail(
                from_email='alina.turganbaeva2019@gmail.com',
                to_emails = 'emma.apigrid@gmail.com',
                subject=SUBJECT,
                plain_text_content=body
            )
            response = sg.send(message)
sendgrid_email_emma()


def sendgrid_email_steven():
    with open('stev.txt','r') as f5:
        steven_list = f5.readlines()
        for line in steven_list:
            body=line
            message=Mail(
                from_email='alina.turganbaeva2019@gmail.com',
                to_emails='maximneveraa@gmail.com',
                subject=SUBJECT,
                plain_text_content=body
            )
            response = sg.send(message)
sendgrid_email_steven()











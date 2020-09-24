import sendgrid
from sendgrid import Mail,Email,Content
sendgrid_api_key = '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'
SUBJECT = 'Hello'
sg = sendgrid.SendGridAPIClient(sendgrid_api_key)

def sendgrid_email(email,name):
    body = 'Hi, '+name
    message = Mail(
        from_email='alina.turganbaeva2019@gmail.com',
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=body)
    response = sg.send(message)
sendgrid_email('alina.turganbaeva2019@gmail.com', 'Alina')

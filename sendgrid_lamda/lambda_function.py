import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def lambda_handler(event, context):
    
    message = Mail(
        from_email='from_email@example.com',
        to_emails='to_email@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>ABCDE</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Send Mail!!')
    }
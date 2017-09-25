import smtplib
from email.mime.text import MIMEText


ACCOUNT_ADR = 'peed.0xDEADBEEF@gmail.com'
ACCOUNT_PWD = 'teampassword'


def create_message(to, subject, message_text):
    """
    Creates a message for an email.
    :param sender: Email address of sender
    :param to: Email address of recipient
    :param subject: Subject of email
    :param message_text: Text of email message
    :return: Base64url encoded email object
    """

    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = ACCOUNT_ADR
    message['subject'] = subject

    return message


def send_message(message):
    """
    Sends message using gmail smtp
    :param message:
    :return:
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(ACCOUNT_ADR, ACCOUNT_PWD)
    text = message.as_string()
    server.sendmail(ACCOUNT_ADR, message['to'], text)
    server.quit()


def main():
    message = create_message('3192900715@vtext.com', 'SMTP Test', 'Test of SMTP Gmail access')
    send_message(message)

if __name__ == '__main__':
    main()

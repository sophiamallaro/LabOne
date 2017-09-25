#!/usr

import argparse
from smtpEmail import create_message, send_message


parser = argparse.ArgumentParser(description="Process strings for email.")
parser.add_argument("to", help="Email address of recipient.", type=str)
parser.add_argument("subject", help="Subject line of email.", type=str)
parser.add_argument("message_text", help="Body text of email.", type=str)
args = parser.parse_args()


def main():
    to = args.to
    subject = args.subject
    message_text = args.message_text

    message = create_message(to, subject, message_text)
    send_message(message)


if __name__ == "__main__":
    main()

import yagmail
import os

sender = 'senderdemo@gmail.com'
receiver = 'afreioxtl@10mail.org'

subject = 'This is the subject'

contents = ["""
Here is the content of the email
Hi!
""",'text.txt']

password = os.getenv('PASSWORD')
if not password:
    print("Error: PASSWORD environment variable not set.")
else:
    print("PASSWORD environment variable is set.")

try:
    yag = yagmail.SMTP(user=sender, password=password)
    print("SMTP client initialized.")

    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")

except Exception as e:
    print(f"An error occurred: {e}")

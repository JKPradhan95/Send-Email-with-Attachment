

import yagmail
import os

sender = 'senderdemo@gmail.com'
receiver = 'g5bdwc3m@flymail.tk'

subject = 'This is the subject'

contents = """
Here is the content of the email
Hi!
"""

password = os.getenv('PSWD')
if not password:
    print("Error: PSWD environment variable not set.")
else:
    print("PSWD environment variable is set.")

try:
    yag = yagmail.SMTP(user=sender, password=password)
    print("SMTP client initialized.")
    
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    
except Exception as e:
    print(f"An error occurred: {e}")

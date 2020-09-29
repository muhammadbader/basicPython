# email = input("Email:")
email = "mhmmdbader9@gmail.com"
# print(email)
# password = getpass.getpass("Password please!!")
password = "whzccbxnqrnbrbgp"
# print(password)

import smtplib
'''
    Sending E-Mails
'''


# smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
# print(smtp_obj.ehlo())

# smtp_obj.ehlo()
# smtp_obj.starttls()

# print(smtp_obj.starttls())
## mhmmdbader9@gmail.com
## my app pass: whzccbxnqrnbrbgp
import getpass ## used to get password instead of input()



# acc = smtp_obj.login(email,password)
# print(acc)

'''
    I want to send to myself
'''


# from_add = email
# to_add = email
# to_add = "nofard@amazon.com"

# subject = input("Enter the subject")
# subject = "test mail"
# subject = "Muhammad Bader- Test Automation Student contract"
# message = input("Enter the body message")
# message = "Hi how are you today!!!"

# message = """
# Hi,
# I am a bit confused about the whole process of getting started.
# Can you explain to em where am I meanwhile and what should be done?
#
#
#
# Thabk you.
# Muhammad
# """
# msg = "Subject: "+subject+'\n'+message # a must format
#
# ans = smtp_obj.sendmail(from_add,to_add,msg)
# print(ans) ## if we get empty {} then the sending was successful
# smtp_obj.quit() ## closing the mail



import imaplib
'''
    Recieving E-Mails
'''



# M = imaplib.IMAP4_SSL("imap.gmail.com")
#
# M.login(email,password)
# # for item in M.list():
# #     for i in item:
# #         print(i)
# M.select('inbox')
#
# # type,data=M.search(None,"BEFORE 01-Nov-2018")
# type,data=M.search(None,'SUBJECT "test mail"')
#
# email_id = data[0]
# result,email_data= M.fetch(email_id,'RFC822')
# # print(email_data)
# raw_email = email_data[0][1]
# raw_email_string = raw_email.decode('utf-8')
#
# import email
# email_message = email.message_from_string(raw_email_string) #this gives a iterartor
#
# for part in email_message.walk():
#     if part.get_content_type()=='text/plain':
#         body = part.get_payload(decode=True)
#         print(body)
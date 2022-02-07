# import messages
# import messages as msg
# from messages import * 
# from messages import show_messages, send_messages
from messages import show_messages as sms, send_messages as send

myList = ['Good afternoon', 'Good evening', 'Good night', 'How are you today']

sms(myList)
sent = send(myList)
sms(sent)

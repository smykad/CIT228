def show_messages(myList):
    for item in myList:
        print(item)

def send_messages(myList):
    ret = []
    for item in myList:
        print(f"Sending message: {item}")
        ret.append(item)        
    return ret

myList = ['Good afternoon', 'Good evening', 'Good night', 'How are you today']

print("List before sending:")
show_messages(myList)

print("Sending messages")
sent_messages = send_messages(myList)

print("Lists after sending:")
print("sent messages:")
show_messages(sent_messages)

print("messages: ")
show_messages(myList)
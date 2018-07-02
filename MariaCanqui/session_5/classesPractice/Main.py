from SMS_store import SMS_store
my_inbox = SMS_store()

def insert_messages():
    my_inbox.add_new_arrival("71342516", "2018-01-23 11:15:09.20", "Text SMS 1")
    my_inbox.add_new_arrival("71342514", "2018-01-23 11:15:09.20", "Text SMS 2")
    my_inbox.add_new_arrival("71342589", "2018-01-23 11:15:09.20", "Text SMS 3")
    my_inbox.add_new_arrival("71342517", "2018-01-23 11:15:09.20", "Text SMS 4")
    my_inbox.add_new_arrival("71342518", "2018-01-23 11:15:09.20", "Text SMS 5")
    my_inbox.add_new_arrival("71342512", "2018-01-23 11:15:09.20", "Text SMS 6")
    my_inbox.add_new_arrival("71342510", "2018-01-23 11:15:09.20", "Text SMS 7")

def get_unread_messages():
    messages = my_inbox.get_unread_indexes()
    return messages

#insert messages
insert_messages()
print("loading messages...")
print(my_inbox.get_messages())
#get unread messages
print("unread messages: ",get_unread_messages())
#message count
print("length: ",my_inbox.message_count())

#get message by id
print("get message 1: ")
print(my_inbox.get_message(1))
print(my_inbox.get_messages())

#delete by id
print("delete 1: ")
print(my_inbox.get_messages())

#delete messages
my_inbox.delete_messages
print(my_inbox.get_messages())



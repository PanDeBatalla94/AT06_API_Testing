class SMS_store:
    def __init__(self):
        self.inbox = {}


    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        sms = {}
        sms["from"] = from_number
        sms["time"] = time_arrived
        sms["text"] = text_of_SMS
        sms["has_been_viewed"] = False
        self.inbox[int(len(self.inbox))+1] = sms

    def message_count(self):
        length = int(len(self.inbox))
        return length

    def get_unread_indexes(self):
        unread = []

        for i in self.inbox:
            if not self.inbox[i]["has_been_viewed"]:
                unread.append(i)
        return unread

    def get_message(self, id):
        if id in self.inbox or self.inbox[id]["text"] == "":
            self.inbox[id]["has_been_viewed"] = True
            return self.inbox.get(id)
        return None

    def get_messages(self):
        return self.inbox

    def delete_message(self, id):
        del self.inbox[id]

    def delete_messages(self):
        del self.inbox


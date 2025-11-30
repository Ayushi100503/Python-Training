class notification:
    def send(self, message):
        print("Sending notification: ", message)

class emailnotification(notification):
    def send(self, message):
        print("Sending email to user: ", message)

class smsnotification(notification):
    def send(self, message):
        print("Sending sms to user: ", message)

class pushnotification(notification):
    def send(self, message):
        print("Sending PUSH notification: ", message)

n1 = emailnotification()
n1.send("Your order is confirmed")

n2 = smsnotification()
n2.send("Your OTP is 1234")

n3 = pushnotification()
n3.send("You have a new message")


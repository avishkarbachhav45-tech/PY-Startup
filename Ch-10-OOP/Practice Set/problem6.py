from random import randint


class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
    def book(avi, fro, to):
        print(f"Ticket is booked in train no: {avi.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(225, 5085)}")


t = Train(155285)
t.book("Nashik-Road", "Pune-Junction")
t.getStatus()
t.getFare("Nashik-Road", "Pune-Junction")

# no change if we change self to slf or self to avi or any other string
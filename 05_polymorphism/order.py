class Order :
    def __init__(self , item , price):
        self.item = item
        self.price = price

    def __gt__(self, ordr2):
        return self.price > ordr2.price


ordr1 = Order("Chips" , 1500)
ordr2 = Order("Tea" , 2000)
print(ordr1.__gt__(ordr2))
print(ordr2.__gt__(ordr1))
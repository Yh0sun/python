class GoodStock:
    def __init__(self, code, stock):
        self.code=code
        self.stock=stock
    def addStock(self, num):
        self.stock +=num
    def aboutGood(self):
        print('상품코드 : ' + self.code)
        print('재고수량 : ' + str(self.stock))

code=input('상품 코드를 입력하세요 : ')
stock=int(input('재고 수량을 입력하세요 : '))

stuff=GoodStock(code, stock)
stuff.aboutGood()
num = int(input('추가할 수량을 입력하시오 : '))
stuff.addStock(num)
print("재고수량 : " + str(stuff.stock))
import datetime as dt
"""class Calculator :
    def __init__(self,limit):
        self.limit= limit
        self.record=[]
    def add_record(self,record):
        self.record.append(record)"""
class Record :
    def __init__(self,amount,comment,date=None):
        self.amount=amount
        self.comment=comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()
    def r(self):
        print(f"{r1.amount} {r1.comment} {self.date}")
for i in range (0,3):
    k1 = 100
    a= int(input())
    b= str(input())
    r1 = Record(amount=a, comment=b)
    r1.r()
    k1 = k1-a
    if k1>0:
        print(f'Можешь тратить , у тебя осталось {k1}р ')
    elif k1==0:
        print(f'Не трать , у тебя осталось 0р ')
    elif k1<0:
        print(f'Можешь тратить , у тебя долг {k1}р ')
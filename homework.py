import datetime as dt
class Calculator :
    def __init__(self,limit):
        self.limit= limit
        self.record=[]
    def add_record(self,record):
        self.record.append(record)
    def get_today_stats(self , Record):
        pass
class Record :
    def __init__(self,amount,comment,date=None):
        self.amount=amount
        self.comment=comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()
print('fdfdfd')
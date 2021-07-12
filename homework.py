import datetime as dt
class Calculator :
    def __init__(self,limit):
        self.limit= limit
        self.records=[]
    def add_record(self,record):
        self.records.append(record)
    def get_today_stats(self):
        today = dt.date.today()
        today1 = sum(record.amount for record in self.records
                          if record.date == today)
        return today1
    def get_week_stats(self):
        today = dt.date.today()
        week_ago = today - dt.timedelta(7)
        week_stats = sum(record.amount for record in self.records
        if week_ago <= record.date <= today)
        return week_stats
    def jjj (self):
        return  self.limit - self.get_today_stats()
class Record :
    def __init__(self,amount,comment,date=None):
        self.amount=amount
        self.comment=comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.jjj()
        if calories >= 0 :
            return (f'В твоем запасе еще  {calories} кКал')
        else:
            return ('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        cash_remained = self.jjj()
        if cash_remained == 0:
            return 'Денег нет , иди на завод'
        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),
        }
        if currency not in currencies:
            return 'такой валюты нет'
        sign, rate = currencies.get(currency)
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            return f'у тебя осталось {cash_remained} {sign}'
        cash_remained = abs(cash_remained)
        return f'Денег нет, держись: твой долг - {cash_remained} {sign}'




from pandas import read_excel


class date:
    def __init__(self, date='', sep='/', **kwargs):
        if date:
            self.date = date
            date = date.split(sep)
            self.day = date[0]
            self.month = date[1]
            self.year = date[2]
        elif all(key in kwargs.keys() for key in ['day', 'month', 'year']):
            self.day = kwargs['day']
            self.month = kwargs['month']
            self.year = kwargs['year']
            self.date = sep.join([self.day, self.month, self.year])
        else:
            raise ValueError("Insufficient Values")

    def __repr__(self):
        return '/'.join([self.day, self.month, self.year])

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.month > other.month:
            return True
        elif self.day > other.day:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.year >= other.year:
            return True
        elif self.month >= other.month:
            return True
        elif self.day >= other.day:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.month < other.month:
            return True
        elif self.day < other.day:
            return True
        else:
            return False

    def __le__(self, other):
        if self.year >= other.year:
            return True
        elif self.month >= other.month:
            return True
        elif self.day >= other.day:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.date == other.date:

            return True
        else:
            return False

    def __ne__(self, other):
        if self.date != other.date:
            return True
        else:
            return False


class item:

    def __init__(self, data):
        self.slno, self.dop, self.firmname, self.pname, self.cat, self.consumption, self.vvn, self.qty, self.unitprice, self.totalprice, self.netprice, self.pgno, = data
        self.values = data

    def __repr__(self):
        return str(self.values)


class records:
    def __init__(self, filename=""):
        if filename:
            df = read_excel(filename)
            self.values = []
            for i, j in df.iterrows():
                l = list(j)
                j[1] = date(j[1].strftime('%Y-%m-%d').replace('-', '/'))
                self.values.append(item(list(j)))
        else:
            self.values = []

    def addRow(self, data):
        self.values.append(item(data))

    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):
        if self.curr < len(self.values):
            res = self.values[self.curr]
            self.curr += 1
            return res
        else:
            raise StopIteration

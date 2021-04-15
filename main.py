class date:
    def __init__(self, date = '', sep = '/', **kwargs):
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
        elif  self.day > other.day:
            return True
        else:
            return False
    
    def __ge__(self, other):
        if self.year >= other.year:
            return True
        elif self.month >= other.month:
            return True
        elif  self.day >= other.day:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.month < other.month:
            return True
        elif  self.day < other.day:
            return True
        else:
            return False
    
    def __le__(self, other):
        if self.year >= other.year:
            return True
        elif self.month >= other.month:
            return True
        elif  self.day >= other.day:
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
            
x = date('01/02/2022')
y = date('01/02/2022')

print(x<y)
